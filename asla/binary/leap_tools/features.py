import numpy as np


class Features:
    """Object that holds all the features"""
    def __init__(self, feat_len, reps):
        """
        :param feat_len: Number of frames collected, before averaging and appending features. Used as number of rows for a given feature matrix
        :type feat_len: int
        :param reps: Number of repetitions to be performed. Used for
        :type reps: int
        """
        self.extended_fingers = np.zeros((feat_len, 5))
        self.tip_length = np.zeros((feat_len, 5))
        self.tip_inner_distances = np.zeros((feat_len, 10))
        self.mcp_length = np.zeros((feat_len, 5))
        self.mcp_inner_distances = np.zeros((feat_len, 10))
        self.pip_length = np.zeros((feat_len, 5))
        self.pip_inner_distances = np.zeros((feat_len, 10))
        self.dip_length = np.zeros((feat_len, 5))
        self.dip_inner_distances = np.zeros((feat_len, 10))
        self.angle_between_tips = np.zeros((feat_len, 10))
        self.angle_between_finger_palm = np.zeros((feat_len, 5))
        self.palm_direction = np.zeros((feat_len, 3))
        self.palm_radius = np.zeros((feat_len, 1))
        self.palm_grab = np.zeros((feat_len, 1))
        self.palm_pinch = np.zeros((feat_len, 1))
        self.palm_normal = np.zeros((feat_len, 3))
        self.rotation_angle = np.zeros(3)
        self.translation = np.zeros(3)
        self.extended_tip_pos_diff = np.zeros(15)
        # shape = reps, num of features + 1(for label)
        self.final_feat = np.zeros((reps, 111))

    def avg_and_append_features(self, curr_label, reps_completed):
        """
        Calculate the average of features for all frames and append it to the final feature list
        :param curr_label: Current label
        :type curr_label: int
        :param reps_completed: Number of repetitions of captured sets
        :type reps_completed: int
        """
        extended_fingers = np.mean(self.extended_fingers, axis=0)
        tip_length = np.mean(self.tip_length, axis=0)
        tip_inner_distances = np.mean(self.tip_inner_distances, axis=0)
        mcp_length = np.mean(self.mcp_length, axis=0)
        mcp_inner_distances = np.mean(self.mcp_inner_distances, axis=0)
        pip_length = np.mean(self.pip_length, axis=0)
        pip_inner_distances = np.mean(self.pip_inner_distances, axis=0)
        dip_length = np.mean(self.dip_length, axis=0)
        dip_inner_distances = np.mean(self.dip_inner_distances, axis=0)
        angle_between_tips = np.mean(self.angle_between_tips, axis=0)
        angle_between_finger_palm = np.mean(self.angle_between_finger_palm, axis=0)
        palm_direction = np.mean(self.palm_direction, axis=0)
        palm_radius = np.mean(self.palm_radius, axis=0)
        palm_grab = np.mean(self.palm_grab, axis=0)
        palm_pinch = np.mean(self.palm_pinch, axis=0)
        palm_normal = np.mean(self.palm_normal, axis=0)
        rotation_angle = self.rotation_angle
        translation = self.translation
        extended_tip_pos_diff = self.extended_tip_pos_diff
        self.final_feat[reps_completed][0] = curr_label
        self.final_feat[reps_completed][1:] = np.concatenate((extended_fingers, tip_length, tip_inner_distances,
                                                              mcp_length, mcp_inner_distances, pip_length,
                                                              pip_inner_distances, dip_length, dip_inner_distances,
                                                              angle_between_tips, angle_between_finger_palm,
                                                              palm_direction, palm_radius, palm_grab, palm_pinch,
                                                              palm_normal, rotation_angle, translation,
                                                              extended_tip_pos_diff), axis=0)
