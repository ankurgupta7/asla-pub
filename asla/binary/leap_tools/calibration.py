from __future__ import division

from PyQt5 import QtCore
from features import Features

import sys
import time
from sys import platform
import numpy as np
import io
import itertools
# from binary.leap_tools.leap import

if platform == "linux" or platform == "linux2":
    if sys.maxsize > 2 ** 32:
        from lib.x64 import Leap
    else:
        from lib.x86 import Leap
elif platform == "darwin":
    from lib import Leap
elif platform == 'win32':
    if sys.maxsize > 2 ** 32:
        from lib.win32.x64 import Leap
    else:
        from lib.win32.x86 import Leap


class Calibration(QtCore.QObject):
    """
    Class to calibrate the sensor
    """
    msg_ready_signal = QtCore.pyqtSignal(str,str,str) # sorry for the ugliness. thats how qt works

    def __init__(self, controller):
        QtCore.QObject.__init__(self)
        self.controller = controller
        self.middle_fingers_params = []
        self.max_inner_distances = []

    def setStatusbar(self, s):
        self.status_bar = s

    def setStatus(self, msg, rep, cur_iter):
        # self.status_bar.showMessage(text)
        self.msg_ready_signal.emit(msg, rep, cur_iter)

        return 0

    def enum(self, **enums):
        return type('Enum', (), enums)

    def calibrate(self, reps=3, skip_time=2, hold_time=5, gap_time=0.25):
        """
        :param reps: Number of repetitions
        :type reps: int
        :param skip_time: The time after which sensor starts capturing
        :type skip_time: int
        :param hold_time: The time person need to hold the hand in position
        :type hold_time: int
        :param gap_time: The time after which frame is captured
        :type gap_time: int
        """
        feat_len = int(hold_time / gap_time)
        features = Features(feat_len, reps)
        reps_completed = 0
        printed = False
        extended = True
        # array of middle finger averages of lengths. size is equal to number of reps
        time_elapsed = 0
        feat_index = 0
        BoneType = self.enum(TYPE_DISTAL=3, TYPE_INTERMEDIATE=2, TYPE_PROXIMAL=1, TYPE_METACARPAL=0)
        while self.controller.is_connected:
            if reps_completed == reps:
                print "Calibration is finished!"
                self.setStatus("Calibration is finished!", str(reps), str(reps_completed))
                self.middle_fingers_params.append(np.mean(features.mcp_length, axis = 0)[2])
                self.middle_fingers_params.append(np.mean(features.pip_length, axis = 0)[2])
                self.middle_fingers_params.append(np.mean(features.dip_length, axis = 0)[2])
                self.middle_fingers_params.append(np.mean(features.tip_length, axis = 0)[2])
                self.max_inner_distances.append(np.mean(features.mcp_inner_distances, axis = 0)[3])
                self.max_inner_distances.append(np.mean(features.pip_inner_distances, axis = 0)[3])
                self.max_inner_distances.append(np.mean(features.dip_inner_distances, axis = 0)[3])
                self.max_inner_distances.append(np.mean(features.tip_inner_distances, axis = 0)[3])
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
                        self.setStatus('Bring hand in view and extend all the fingers', str(reps), str(reps_completed))
                        printed = True
                        extended = True
                elif feat_index < feat_len:
                    for hand in hands:
                        # only for right hand as of now
                        if hand.is_right and time_elapsed > skip_time:
                            ordered_finger_list = []
                            pointables = hand.pointables
                            if len(pointables.extended()) != 5:
                                self.setStatus("Please extend all the fingers for calibration", str(reps), str(reps_completed))
                                print "Please extend all the fingers for calibration"
                                extended = True
                            else:
                                if extended:
                                    self.setStatus("Good! Calibration is starting. Do NOT move the hand...", str(reps), str(reps_completed))
                                    print "Good! Calibration is starting. Do NOT move the hand..."
                                    time.sleep(10 * gap_time)
                                    extended = False
                                # Relative origin(used to calculate the relative distances)
                                for pointable in pointables:
                                    finger = Leap.Finger(pointable)
                                    ordered_finger_list.insert(finger.type, finger)

                                self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_DISTAL)
                                self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_INTERMEDIATE)
                                self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_PROXIMAL)
                                self.set_lengths(features, feat_index, ordered_finger_list, hand, BoneType.TYPE_METACARPAL)

                                self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_DISTAL)
                                self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_INTERMEDIATE)
                                self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_PROXIMAL)
                                self.set_inner_distances(features, feat_index, ordered_finger_list, BoneType.TYPE_METACARPAL)

                                feat_index += 1
                elif feat_index == feat_len:
                    feat_index += 1
                    reps_completed += 1
                    self.setStatus("Remove hand from view", str(reps), str(reps_completed))
                    print "Remove hand from view"
                    printed = False
                    extended = False
                time.sleep(gap_time)
                time_elapsed += gap_time

    def write_calibration(self):
        """
        Writes calibration parameters to file
        """
        with io.FileIO("calibration_data.txt", "w") as cal_file:
            cal_file.write("middle finger parameters: " +
                           str(self.middle_fingers_params) +"\n" +
                           "inner distances parameters: " + str(self.max_inner_distances))

    @staticmethod
    def set_inner_distances(features, feat_index, list_of_fingers, type):
        bone_list = []
        for finger in list_of_fingers:
            bone_list.append(finger.bone(type))
        combinations = list(itertools.combinations(bone_list, 2))
        for comb, position in zip(combinations, range(len(combinations))):
            finger1 = comb[0].next_joint
            finger2 = comb[1].next_joint
            inner = (finger1 - finger2).magnitude
            if type == 3:
                features.tip_inner_distances[feat_index][position] = inner
            elif type == 2:
                features.dip_inner_distances[feat_index][position] = inner
            elif type == 1:
                features.pip_inner_distances[feat_index][position] = inner
            elif type == 0:
                features.mcp_inner_distances[feat_index][position] = inner

    @staticmethod
    def set_lengths(features, feat_index, list_of_fingers, hand, type):
        palm_center = hand.stabilized_palm_position
        bone_list = []
        for finger in list_of_fingers:
            bone_list.append(finger.bone(type))
        for bone, finger in zip(bone_list, list_of_fingers):
            if type == 3:
                features.tip_length[feat_index][finger.type] = (bone.next_joint - palm_center).magnitude
            elif type == 2:
                features.dip_length[feat_index][finger.type] = (bone.next_joint - palm_center).magnitude
            elif type == 1:
                features.pip_length[feat_index][finger.type] = (bone.next_joint - palm_center).magnitude
            elif type == 0:
                features.mcp_length[feat_index][finger.type] = (bone.next_joint - palm_center).magnitude
