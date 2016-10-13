from __future__ import division
import inspect
import os
import sys
import time
from sys import platform
import numpy as np

if platform == "linux" or platform == "linux2":
    src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    arch_dir = './lib/x64' if sys.maxsize > 2 ** 32 else './lib/x86'
    sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
elif platform == "darwin":
    src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    lib_dir = os.path.abspath(os.path.join(src_dir, './lib'))
    sys.path.insert(0, lib_dir)

import Leap


class ExpertGestureCollection:
    def __init__(self, label):
        self.label = label
        self.controller = Leap.Controller()
        pass

    def wait_for_connection(self):
        """
        Wait for Controller to be connected to the device.
        """
        while not self.controller.is_connected:
            pass
        print 'Controller CONNECTED'

    def extract_features(self, reps=5, skip_time=2, hold_time=4, gap_time=0.25):
        feat_len = int(hold_time / gap_time)
        feat_index = 0
        features = Features(feat_len, reps)
        reps_completed = 0
        printed = False
        while self.controller.is_connected:
            if reps_completed == reps:
                return features.final_feat
            else:
                frame = self.controller.frame()
                hands = frame.hands
                if len(hands) == 0:
                    feat_index = 0
                    time_elapsed = 0
                    if not printed:
                        print 'Bring hand in view'
                        printed = True
                elif feat_index < feat_len:
                    for hand in hands:
                        # only for right hand as of now
                        if hand.is_right and time_elapsed > skip_time:
                            pointables = frame.pointables
                            # Relative origin(used to calculate the relative distances)
                            hand_center = hand.stabilized_palm_position
                            for pointable in pointables:
                                finger = Leap.Finger(pointable)
                                if finger.is_extended:
                                    features.extended_fingers[feat_index][finger.type] = 1.0
                                    pointable_pos = pointable.stabilized_tip_position
                                    relative_pos = pointable_pos - hand_center
                                    features.finger_lengths[feat_index][finger.type] = relative_pos.magnitude
                            print "Extended Fingers", features.extended_fingers[feat_index]
                            print "Finger lengths", features.finger_lengths[feat_index]
                            feat_index += 1
                elif feat_index == feat_len:
                    feat_index += 1
                    features.avg_and_append_features(int(self.label), reps_completed)
                    reps_completed += 1
                    print "Remove hand from view"
                    printed = False
            time.sleep(gap_time)
            time_elapsed += gap_time


# todo
# Maybe make a separate class later or maybe not :)
# Add python properties(for getters and setters)
class Features:
    def __init__(self, feat_len, reps):
        self.feat_len = feat_len
        self.extended_fingers = np.zeros((self.feat_len, 5))
        self.finger_lengths = np.zeros((self.feat_len, 5))
        self.final_feat = np.zeros((reps, 11))

    def avg_and_append_features(self, curr_label, reps_completed):
        feat1 = np.mean(self.extended_fingers, axis=0)
        feat2 = np.mean(self.finger_lengths, axis=0)
        self.final_feat[reps_completed][0] = curr_label
        self.final_feat[reps_completed][1:] = np.append(feat1, feat2)