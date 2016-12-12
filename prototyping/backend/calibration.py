from __future__ import division
import inspect
import os
import sys
import time
from sys import platform
import numpy as np
import io

if platform == "linux" or platform == "linux2":
    src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    arch_dir = './lib/x64' if sys.maxsize > 2 ** 32 else './lib/x86'
    sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
elif platform == "darwin":
    src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    lib_dir = os.path.abspath(os.path.join(src_dir, './lib'))
    sys.path.insert(0, lib_dir)

import Leap
from features import Features


class Calibration:
    def __init__(self, controller):
        self.controller = controller
        self.middle_len = 1
        self.max_inner_dist = 1
        pass

    def calibrate(self, reps=3, skip_time=2, hold_time=5, gap_time=0.25):
        feat_len = int(hold_time / gap_time)
        features = Features(feat_len, reps)
        reps_completed = 0
        printed = False
        extended = True
        index_middle_finger = 2
        # array of middle finger averages of lengths. size is equal to number of reps
        middle_len = []
        time_elapsed = 0
        feat_index = 0
        while self.controller.is_connected:
            if reps_completed == reps:
                print "Calibration is finished!"
                self.middle_len = np.mean(middle_len)
                self.write_calibration()
                return
            else:
                frame = self.controller.frame()
                hands = frame.hands
                if len(hands) == 0:
                    feat_index = 0
                    time_elapsed = 0
                    if not printed:
                        print 'Bring hand in view and extend all the fingers'
                        printed = True
                        extended = True
                elif feat_index < feat_len:
                    for hand in hands:
                        # only for right hand as of now
                        if hand.is_right and time_elapsed > skip_time:
                            pointables = frame.pointables
                            if len(pointables.extended()) != 5:
                                print "Please extend all the fingers for calibration"
                                extended = True
                            else:
                                if extended:
                                    print "Good! Calibration is starting. Do NOT move the hand..."
                                    #time.sleep(10 * gap_time)
                                    extended = False
                                # Relative origin(used to calculate the relative distances)
                                hand_center = hand.stabilized_palm_position
                                for pointable in pointables:
                                    finger = Leap.Finger(pointable)
                                    pointable_pos = pointable.stabilized_tip_position
                                    relative_pos = pointable_pos - hand_center
                                    features.finger_lengths[feat_index][finger.type] = relative_pos.magnitude
                                print "Finger lengths", features.finger_lengths[feat_index]
                                feat_index += 1
                elif feat_index == feat_len:
                    feat_index += 1
                    middle_len.append(np.mean(features.finger_lengths, axis=0)[index_middle_finger])
                    reps_completed += 1
                    print "Remove hand from view"
                    printed = False
                    extended = False
                time.sleep(gap_time)
                time_elapsed += gap_time

    def write_calibration(self):
        with io.FileIO("calibration_data_damian.txt", "w") as cal_file:
            cal_file.write("middle_len " + str(self.middle_len))
