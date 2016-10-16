from __future__ import division
import inspect
import os
import sys
import time
from sys import platform
import itertools
from features import Features

if platform == "linux" or platform == "linux2":
    src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    arch_dir = './lib/x64' if sys.maxsize > 2 ** 32 else './lib/x86'
    sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
elif platform == "darwin":
    src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    lib_dir = os.path.abspath(os.path.join(src_dir, './lib'))
    sys.path.insert(0, lib_dir)

import Leap


class UserGesturePrediction:
    def __init__(self, model, scaler):
        self.controller = Leap.Controller()
        self.model = model
        self.scaler = scaler
        self.predicted_label = None
        pass

    def wait_for_connection(self):
        """
        Wait for Controller to be connected to the device.
        """
        while not self.controller.is_connected:
            pass
        print 'Controller CONNECTED'

    def extract_features(self, cal_param=1, reps=1, skip_time=0.5, hold_time=1, gap_time=0.25):
        feat_len = int(hold_time / gap_time)
        feat_index = 0
        time_elapsed = 0
        features = Features(feat_len, reps)
        reps_completed = 0
        printed = False
        to_predict = None
        while self.controller.is_connected:
            if reps_completed == reps:
                to_predict = features.final_feat[0][1:].reshape(1, -1)
                to_predict_scaled = self.scaler.transform(to_predict)
                self.predicted_label = self.model.predict(to_predict_scaled)
                return
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
                            # palm direction feature
                            features.palm_direction[feat_index] = hand.direction.to_tuple()
                            # palm sphere radius
                            features.palm_radius[feat_index] = hand.sphere_radius
                            # hand grab strength
                            features.palm_grab[feat_index] = hand.grab_strength
                            # hand pinch strength
                            features.palm_pinch[feat_index] = hand.pinch_strength
                            # inner_distances features
                            combinations = list(itertools.combinations(pointables, 2))
                            for comb, position in zip(combinations, range(len(combinations))):
                                finger1 = comb[0].stabilized_tip_position
                                finger2 = comb[1].stabilized_tip_position
                                inner_tip = (finger1 - finger2).magnitude
                                features.inner_distances[feat_index][position] = inner_tip

                        # Relative origin(used to calculate the relative distances)
                            hand_center = hand.stabilized_palm_position
                            for pointable in pointables:
                                finger = Leap.Finger(pointable)
                                if finger.is_extended:
                                    features.extended_fingers[feat_index][finger.type] = 1.0
                                    pointable_pos = pointable.stabilized_tip_position
                                    relative_pos = pointable_pos - hand_center
                                    # Scaling the lengths of fingers to the length of middle finger (cal_param)
                                    features.finger_lengths[feat_index][finger.type] = relative_pos.magnitude/cal_param
                            print "Extended Fingers", features.extended_fingers[feat_index]
                            print "Finger lengths", features.finger_lengths[feat_index]
                            print "Inter distances between tips", features.inner_distances[feat_index]
                            print "Palm direction", features.palm_direction[feat_index]
                            print "Palm sphere radius", features.palm_radius[feat_index]
                            print "Palm grab strength", features.palm_grab[feat_index]
                            print "Palm pinch strength", features.palm_pinch[feat_index]
                            feat_index += 1
                elif feat_index == feat_len:
                    feat_index += 1
                    features.avg_and_append_features(None, reps_completed)
                    reps_completed += 1
                    print "Remove hand from view"
                    printed = False
                time.sleep(gap_time)
                time_elapsed += gap_time



