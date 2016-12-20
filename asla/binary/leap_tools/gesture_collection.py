from __future__ import division

from features import Features
from calibration import Calibration

from PyQt5 import QtCore
import sys
import time
from sys import platform
import itertools
import math
import numpy as np

if platform == "linux" or platform == "linux2":
    if sys.maxsize > 2 ** 32:
        from lib.x64 import Leap
        from lib.x64.Leap import Vector
    else:
        from lib.x86 import Leap
        from lib.x86.Leap import Vector
elif platform == "darwin":
    from lib import Leap
    from lib.Leap import Vector
elif platform == 'win32':
    if sys.maxsize > 2 ** 32:
        from lib.win32.x64 import Leap
        from lib.win32.x64.Leap import Vector
    else:
        from lib.win32.x86 import Leap
        from lib.win32.x86.Leap import Vector


class GestureCollection(QtCore.QObject):
    """
    Extracting the features from captured gesture
    """
    msg_ready_signal = QtCore.pyqtSignal(str) # sorry for the ugliness. thats how qt works
    iter_rep_signal = QtCore.pyqtSignal(str, str, str)

    def __init__(self, label):
        QtCore.QObject.__init__(self)
        self.label = ord(label.upper()) - 64
        self.controller = Leap.Controller()
        self.calibration = Calibration(self.controller)
        self.status = None
        self.status_bar = None
        self.status_mutex = False
        self.stop_thread_flag = False
        self.stop_thread_mutex = False

    def set_stop_thread_flag(self, stop=True):
        while self.stop_thread_mutex:
            continue
        self.stop_thread_mutex = True
        self.stop_thread_flag = stop
        self.stop_thread_mutex = False

    def get_stop_thread_flag(self):
        while self.stop_thread_mutex:
            continue
        return self.stop_thread_flag

    def setStatus(self, text):
        self.msg_ready_signal.emit(text)
        # while(self.status_mutex):
        #     print 'waiting for lock/ set status'
        #     continue
        self.status_mutex = True
        self.status = text
        self.status_mutex = False
        # self.status_bar.showMessage(text)

    def send_iter_rep_to_process(self, msg, rep, cur_iter):
        self.iter_rep_signal.emit(msg, str(rep), str(cur_iter))

    def getStatus(self):
        # while (self.status_mutex):
        #     print 'waiting for lock/ get status'
        #     continue
        self.status_mutex = True
        b = (self.status + '.')[:-1] # creating a deep copy of string. the neatest way to do that sadly.
        self.status_mutex = False
        return b

    def setStatusBar(self, s):
        self.status_bar = s
        self.calibration.setStatusbar(s)

    def is_calibrated(self):
        """
        Checks if the sensor is calibrated
        :return: True if calibrated, False if not
        :rtype: boolean
        """
        try:
            in_file = open('calibration_data.txt', 'r')
            # self.setStatus('test. will crash if not handled properly')
            lines = in_file.readlines()
            for index in range(len(lines)):
                field_name, field_val = lines[index].split(":")
                field_val = field_val.strip(' []\n')
                field_val = map(float, field_val.split(','))
                if index == 0:
                    self.calibration.middle_fingers_params= np.asarray(field_val)
                if index == 1:
                    self.calibration.max_inner_distances = np.asarray(field_val)
            return True
        except IOError:
            self.setStatus('calibration file not found. will start calibration now')
            return False
        except ValueError:
            self.setStatus('something weird with the calibration data happened')
            return False

    def wait_for_connection(self):
        """
        Wait for Controller to be connected to the device.
        """
        if not self.controller.is_connected:
            self.setStatus("Leap Not Connected!")
            return False
        print 'Controller CONNECTED'
        return True

    # enums for bone types
    def enum(self, **enums):
        return type('Enum', (), enums)

    def extract_features(self, reps=3, skip_time=1.5, hold_time=2, gap_time=0.25, print_feat=True):
        """Method to extract features
        :return: final feature list
        :rtype: list
        """

        BoneType = self.enum(TYPE_DISTAL=3, TYPE_INTERMEDIATE=2, TYPE_PROXIMAL=1, TYPE_METACARPAL=0)
        feat_len = int(hold_time / gap_time)
        feat_index = 0
        time_elapsed = 0
        features = Features(feat_len, reps)
        reps_completed = 0
        printed = False
        start_frame = None

        while self.controller.is_connected:

            if self.get_stop_thread_flag():
                return features.final_feat
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
                        self.setStatus('Bring hand in view')
                        printed = True
                elif feat_index < feat_len:
                    for hand in hands:
                        # only for right hand as of now
                        if hand.is_right and time_elapsed > skip_time:
                            ordered_finger_list = []
                            ordered_pointable_list = []
                            pointables = hand.pointables
                            for pointable in pointables:
                                finger = Leap.Finger(pointable)
                                ordered_finger_list.insert(finger.type, finger)
                                ordered_pointable_list.insert(finger.type, pointable)

                            # setting up features related to hand only
                            self.set_hand_features(features, feat_index, hand)

                            # setting up the boolean vector of extended fingers
                            self.set_extended_fingers(features, feat_index, ordered_finger_list)

                            # setting up the lengths of bones
                            # needs to be refactored
                            self.set_lengths(features, feat_index, ordered_finger_list,hand,  BoneType.TYPE_DISTAL)
                            self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_INTERMEDIATE)
                            self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_PROXIMAL)
                            self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_METACARPAL)

                            # setting up the inner distances between all types of bones
                            # needs to be refactored in feature (too long list of same parameters)
                            self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_DISTAL)
                            self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_INTERMEDIATE)
                            self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_PROXIMAL)
                            self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_METACARPAL)

                            # setting up the angles between the fingers (degrees)
                            self.set_angle_between_tips(features, feat_index, ordered_finger_list)

                            # setting up the angles between the fingers and palm plane (degrees)
                            self.set_angle_between_fingers_and_palm(features, feat_index, ordered_finger_list, hand)

                            # Movement features:
                            if not start_frame:
                                print 'Capturing First Frame'
                                start_frame = frame
                                printed = False
                            elif feat_index == feat_len - 1:
                                end_frame = frame
                                self.set_movement_features(features, start_frame, end_frame, hand)
                                if print_feat:
                                    self.print_dynamic_features(features)
                            if print_feat:
                                self.print_static_features(features, feat_index)
                            feat_index += 1
                elif feat_index == feat_len:
                    feat_index += 1
                    features.avg_and_append_features(int(self.label), reps_completed)
                    reps_completed += 1
                    print "Remove hand from view"
                    self.setStatus("Remove hand from view")
                    self.send_iter_rep_to_process("Remove hand from view", str(reps), str(reps_completed))
                    printed = False
                if len(hands) != 0:
                    time.sleep(gap_time)
                    time_elapsed += gap_time

    @staticmethod
    def set_extended_fingers(features, feat_index, list_of_fingers):
        for finger in list_of_fingers:
            if finger.is_extended:
                features.extended_fingers[feat_index][finger.type] = 1.0
            else:
                features.extended_fingers[feat_index][finger.type] = 0

    def set_inner_distances(self, features, feat_index, list_of_fingers, type):
        bone_list = []
        for finger in list_of_fingers:
            bone_list.append(finger.bone(type))
        combinations = list(itertools.combinations(bone_list, 2))
        for comb, position in zip(combinations, range(len(combinations))):
            finger1 = comb[0].next_joint
            finger2 = comb[1].next_joint
            inner = (finger1 - finger2).magnitude
            if type == 3:
                features.tip_inner_distances[feat_index][position] = inner/self.calibration.max_inner_distances[type]
            elif type == 2:
                features.dip_inner_distances[feat_index][position] = inner/self.calibration.max_inner_distances[type]
            elif type == 1:
                features.pip_inner_distances[feat_index][position] = inner/self.calibration.max_inner_distances[type]
            elif type == 0:
                features.mcp_inner_distances[feat_index][position] = inner/self.calibration.max_inner_distances[type]

    @staticmethod
    def set_angle_between_tips(features, feat_index, list_of_fingers):
        combinations = list(itertools.combinations(list_of_fingers, 2))
        for comb, position in zip(combinations, range(len(combinations))):
            finger1 = comb[0]
            finger2 = comb[1]
            inner_angle = (finger1.direction.angle_to(finger2.direction))
            features.angle_between_tips[feat_index][position] = inner_angle * 180/math.pi;

    @staticmethod
    def set_angle_between_fingers_and_palm(features, feat_index, list_of_fingers, hand):
        palm_normal = hand.palm_normal
        for finger in list_of_fingers:
            features.angle_between_finger_palm[feat_index][finger.type] = \
                finger.direction.angle_to(palm_normal) * 180/math.pi

    def set_lengths(self, features, feat_index, list_of_fingers,hand, type):
        palm_center = hand.stabilized_palm_position
        bone_list = []
        for finger in list_of_fingers:
            bone_list.append(finger.bone(type))
        for bone, finger in zip(bone_list, list_of_fingers):
            if type == 3:
                features.tip_length[feat_index][finger.type] =\
                    (bone.next_joint - palm_center).magnitude/self.calibration.middle_fingers_params[type]
            elif type == 2:
                features.dip_length[feat_index][finger.type] = \
                    (bone.next_joint - palm_center).magnitude/self.calibration.middle_fingers_params[type]
            elif type == 1:
                features.pip_length[feat_index][finger.type] = \
                    (bone.next_joint - palm_center).magnitude/self.calibration.middle_fingers_params[type]
            elif type == 0:
                features.mcp_length[feat_index][finger.type] = \
                    (bone.next_joint - palm_center).magnitude/self.calibration.middle_fingers_params[type]

    @staticmethod
    def set_hand_features(features, feat_index, hand):
        features.palm_direction[feat_index] = hand.direction.to_tuple()
        features.palm_radius[feat_index] = hand.sphere_radius
        features.palm_grab[feat_index] = hand.grab_strength
        features.palm_pinch[feat_index] = hand.pinch_strength
        features.palm_normal[feat_index] = hand.palm_normal.to_tuple()

    @staticmethod
    def set_movement_features(features, start_frame, end_frame, hand):
        features.rotation_angle = [hand.rotation_angle(start_frame, Vector.x_axis),
                                   hand.rotation_angle(start_frame, Vector.y_axis),
                                   hand.rotation_angle(start_frame, Vector.z_axis)]
        features.translation = [hand.translation(start_frame).x, hand.translation(start_frame).y, hand.translation(start_frame).z]
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
                            features.extended_tip_pos_diff[start_type*3: (start_type+1)*3] = diff.to_float_array()

    @staticmethod
    def print_static_features(features, feat_index):
        print "Extended Fingers", features.extended_fingers[feat_index]
        print "Tip Length", features.tip_length[feat_index]
        print "Tip inner distances", features.tip_inner_distances[feat_index]
        print "Dip Length", features.dip_length[feat_index]
        print "Dip inner distances", features.dip_inner_distances[feat_index]
        print "Pip Length", features.pip_length[feat_index]
        print "Pip inner distances", features.pip_inner_distances[feat_index]
        print "Mcp Length", features.mcp_length[feat_index]
        print "Mcp inner distances", features.mcp_inner_distances[feat_index]
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