from __future__ import division
import sys
import time
from sys import platform
import itertools
from features import Features
from calibration import Calibration

if platform == "linux" or platform == "linux2":
    if sys.maxsize > 2 ** 32:
        from lib.x64 import Leap
    else:
        from lib.x86 import Leap
elif platform == "darwin":
    from lib import Leap
    from lib.Leap import Vector


class GestureCollection:
    """
    Extracting the features from captured gesture
    """
    def __init__(self, label=-1):
        self.label = label
        self.controller = Leap.Controller()
        self.calibration = Calibration(self.controller)
        pass

    def is_calibrated(self):
        """
        Checks if the sensor is calibrated
        :return: True if calibrated, False if not
        :rtype: boolean
        """
        try:
            in_file = open('calibration_data.txt', 'r')
            lines = in_file.readlines()
            for line in lines:
                field_name, field_val = line.rstrip('\n').split()
                self.calibration.middle_len = float(field_val)
            return True
        except IOError:
            return False

    def wait_for_connection(self):
        """
        Wait for Controller to be connected to the device.
        """
        while not self.controller.is_connected:
            pass
        print 'Controller CONNECTED'

    def extract_features(self, reps=5, skip_time=2, hold_time=5, gap_time=0.25, print_feat=True):
        """Method to extract features
        :return: final feature list
        :rtype: list
        """
        feat_len = int(hold_time / gap_time)
        feat_index = 0
        time_elapsed = 0
        features = Features(feat_len, reps)
        reps_completed = 0
        printed = False
        start_frame = None
        while self.controller.is_connected:
            if reps_completed == reps:
                return features.final_feat
            else:
                frame = self.controller.frame()
                hands = frame.hands
                if len(hands) == 0:
                    feat_index = 0
                    time_elapsed = 0
                    start_frame = None
                    if not printed:
                        print 'Bring hand in view'
                        printed = True
                elif feat_index < feat_len:
                    for hand in hands:
                        # only for right hand as of now
                        if hand.is_right and time_elapsed > skip_time:
                            hand_center = hand.stabilized_palm_position
                            pointables = frame.pointables
                            fingers = frame.fingers
                            self.set_hand_features(features, feat_index, hand)
                            self.set_inner_distances(fingers, 3)

                            # Movement features:
                            if not start_frame:
                                print 'Capturing First Frame'
                                start_frame = frame
                                printed = False
                            elif feat_index == feat_len - 1:
                                end_frame = frame
                                self.set_movement_features(features, start_frame, end_frame)
                                if print_feat:
                                    self.print_dynamic_features(features)

                            for pointable in pointables:
                                finger = Leap.Finger(pointable)
                                if finger.is_extended:
                                    features.extended_fingers[feat_index][finger.type] = 1.0
                                    pointable_pos = pointable.stabilized_tip_position
                                    relative_pos = pointable_pos - hand_center
                                    # Scaling the lengths of fingers to the length of middle finger (cal_param)
                                    features.finger_lengths[feat_index][finger.type] = \
                                        relative_pos.magnitude/self.calibration.middle_len
                            if print_feat:
                                self.print_static_features(features, feat_index)
                            feat_index += 1
                elif feat_index == feat_len:
                    feat_index += 1
                    features.avg_and_append_features(int(self.label), reps_completed)
                    reps_completed += 1
                    print "Remove hand from view"
                    printed = False
                time.sleep(gap_time)
                time_elapsed += gap_time

    @staticmethod
    def set_inner_distances(features, feat_index, list_of_fingers, type):
        bone_list = []
        for finger in list_of_fingers:
            bone_list.append(finger.bone(type))
        combinations = list(itertools.combinations(bone_list, 2))
        for comb, position in zip(combinations, range(len(combinations))):
            finger1 = comb[position].next_joint
            finger2 = comb[position].next_joint
            inner = (finger1 - finger2).magnitude
            features.inner_distances[feat_index][position] = inner

            # Relative origin(used to calculate the relative distances)

    @staticmethod
    def set_hand_features(features, feat_index, hand):
        features.palm_direction[feat_index] = hand.direction.to_tuple()
        features.palm_radius[feat_index] = hand.sphere_radius
        features.palm_grab[feat_index] = hand.grab_strength
        features.palm_pinch[feat_index] = hand.pinch_strength
        features.palm_normal[feat_index] = hand.palm_normal

    @staticmethod
    def set_movement_features(features, start_frame, end_frame):
        hand = end_frame.hand
        features.rotation_angle = [hand.rotation_angle(start_frame, Vector.x_axis),
                                   hand.rotation_angle(start_frame, Vector.y_axis),
                                   hand.rotation_angle(start_frame, Vector.z_axis)]
        features.translation = hand.translation(start_frame)
        start_pointables = start_frame.pointables
        end_pointables = end_frame.pointables
        for s_p in start_pointables:
            if s_p.is_extended:
                start_pos = s_p.stabilized_tip_position
                start_type = Leap.Finger(s_p).type
                for e_p in end_pointables:
                    if e_p.is_extended:
                        if Leap.Finger(e_p).type == start_type:
                            end_pos = e_p.stabilized_tip_position
                            diff = end_pos - start_pos
                            features.extended_tip_pos_diff[start_type*3: (start_type+1)*3] = diff

    @staticmethod
    def print_static_features(features, feat_index):
        print "Extended Fingers", features.extended_fingers[feat_index]
        print "Tip Length", features.tip_length[feat_index]
        print "Tip inner distances", features.inner_distances[feat_index]
        print "Mcp Length", features.mcp_length[feat_index]
        print "Mcp inner distances", features.mcp_inner_distances[feat_index]
        print "Pip Length", features.pip_inner_distances[feat_index]
        print "Pip inner distances", features.pip_length[feat_index]
        print "Dip Length", features.dip_length[feat_index]
        print "Dip inner distances", features.dip_inner_distances[feat_index]
        print "Angle between tips", features.angle_between_tips[feat_index]
        print "Angle between fingers and palm", features.angle_between_finger_palm[feat_index]

        print "Palm direction", features.palm_direction[feat_index]
        print "Palm sphere radius", features.palm_radius[feat_index]
        print "Palm grab strength", features.palm_grab[feat_index]
        print "Palm pinch strength", features.palm_pinch[feat_index]
        print "Palm normal", features.palm_normal[feat_index]

    @staticmethod
    def print_dynamic_features(features):
        print "Rotation Angle", features.rotation_angle
        print "Translation", features.translation
        print "Extended Tip Pos Diff", features.extended_tip_pos_diff