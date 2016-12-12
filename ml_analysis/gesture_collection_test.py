from __future__ import division
import inspect
import os
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
    # src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    # arch_dir = './lib/x64' if sys.maxsize > 2 ** 32 else './lib/x86'
    # sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
elif platform == "darwin":
    from lib import Leap
    from lib.Leap import Vector
    from lib.Leap import Bone
    # src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    # lib_dir = os.path.abspath(os.path.join(src_dir, './lib'))
    # sys.path.insert(0, lib_dir)

# import Leap


class GestureCollection:
    """
    To test how to capture features
    """
    def __init__(self, label=-1):
        self.label = label
        self.controller = Leap.Controller()
        # self.calibration = Calibration(self.controller)
        pass

    # def is_calibrated(self):
    #     """
    #     Checks if the sensor is calibrated
    #     :return: True if calibrated, False if not
    #     :rtype: boolean
    #     """
    #     try:
    #         in_file = open('calibration_data_damian.txt', 'r')
    #         lines = in_file.readlines()
    #         for line in lines:
    #             field_name, field_val = line.rstrip('\n').split()
    #             self.calibration.middle_len = float(field_val)
    #         return True
    #     except IOError:
    #         return False

    def wait_for_connection(self):
        """
        Wait for Controller to be connected to the device.
        """
        while not self.controller.is_connected:
            pass
        print 'Controller CONNECTED'

    def extract_features(self, reps=5, skip_time=1, hold_time=2, gap_time=0.25, print_feat=True):
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
        first_frame = None
        while self.controller.is_connected:
            if reps_completed == reps:
                return
            else:
                frame = self.controller.frame()
                hands = frame.hands
                if len(hands) == 0:
                    feat_index = 0
                    time_elapsed = 0
                    first_frame = None
                    if not printed:
                        print 'Bring hand in view'
                        printed = True
                elif feat_index < feat_len:
                    for hand in hands:
                        # only for right hand as of now
                        if hand.is_right and time_elapsed > skip_time:
                            if not first_frame:
                                print 'Capturing First Frame'
                                first_frame = frame
                                printed = False
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
                            # combinations = list(itertools.combinations(pointables, 2))
                            # for comb, position in zip(combinations, range(len(combinations))):
                            #     finger1 = comb[0].stabilized_tip_position
                            #     finger2 = comb[1].stabilized_tip_position
                            #     inner_tip = (finger1 - finger2).magnitude
                            #     features.inner_distances[feat_index][position] = inner_tip

                        # Relative origin(used to calculate the relative distances)
                            hand_center = hand.stabilized_palm_position
                            for pointable in pointables:
                                finger = Leap.Finger(pointable)
                                print finger.type
                                mcp_rel_pos = finger.bone(Bone.TYPE_METACARPAL).next_joint - hand_center
                                pip_rel_pos = finger.bone(Bone.TYPE_PROXIMAL).next_joint - hand_center
                                dip_rel_pos = finger.bone(Bone.TYPE_INTERMEDIATE).next_joint - hand_center
                                tip_rel_pos = finger.bone(Bone.TYPE_DISTAL).next_joint - hand_center
                                if finger.type == 0:
                                    thumb_mcp = mcp_rel_pos
                                elif finger.type == 4:
                                    pinky_mcp = mcp_rel_pos
                                    # print 'MAX_MCP',(pinky_mcp - thumb_mcp).magnitude
                                # print 'mcp', mcp_rel_pos.magnitude
                                # print 'pip', pip_rel_pos.magnitude
                                # print 'dip', dip_rel_pos.magnitude
                                # print 'tip', tip_rel_pos.magnitude

                                if finger.is_extended:

                                    # This is basically the tip
                                    # print 'DISTAL', finger.bone(Bone.TYPE_DISTAL).next_joint
                                    features.extended_fingers[feat_index][finger.type] = 1.0
                                    pointable_pos = pointable.stabilized_tip_position
                                    relative_pos = pointable_pos - hand_center
                                    # Scaling the lengths of fingers to the length of middle finger (cal_param)
                                    # features.finger_lengths[feat_index][finger.type] = \
                                     #   relative_pos.magnitude# /self.calibration.middle_len
                            # if print_feat:
                                # print "Extended Fingers", features.extended_fingers[feat_index]
                                # print "Finger lengths", features.finger_lengths[feat_index]
                                # print "Inter distances between tips", features.inner_distances[feat_index]
                                # print "Palm direction", features.palm_direction[feat_index]
                                # print "Palm sphere radius", features.palm_radius[feat_index]
                                # print "Palm grab strength", features.palm_grab[feat_index]
                                # print "Palm pinch strength", features.palm_pinch[feat_index]
                                # print "PALM WIDTH", hand.palm_width
                            feat_index += 1
                elif feat_index == feat_len:
                    # print "Rotation Matrix?? ", hand.rotation_matrix(first_frame)
                    # print "Rotation Angle y ", hand.rotation_angle(first_frame, Vector.y_axis)
                    # print "Rotation Angle x ", hand.rotation_angle(first_frame, Vector.x_axis)
                    # print "Rotation Angle z ", hand.rotation_angle(first_frame, Vector.z_axis)
                    print "Translation ", hand.translation(first_frame)
                    start_pointables = first_frame.pointables
                    end_pointables = frame.pointables
                    for p in start_pointables:
                        start_pos = p.stabilized_tip_position
                        type1 = Leap.Finger(p).type
                        print type1
                        print 3*type1, 3*type1 + 1, 3*type1 + 2
                        for p1 in end_pointables:
                            if Leap.Finger(p1).type == type1:
                                end_pos = p1.stabilized_tip_position
                                diff = end_pos - start_pos
                                print diff
                    feat_index += 1
                    features.avg_and_append_features(int(self.label), reps_completed)
                    reps_completed += 1
                    print "Remove hand from view"
                    printed = False
                time.sleep(gap_time)
                time_elapsed += gap_time

if __name__ == "__main__":
    gc = GestureCollection()
    print "waiting for connection"
    gc.wait_for_connection()
    gc.extract_features()
