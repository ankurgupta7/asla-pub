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
        self.feat_len = feat_len
        self.extended_fingers = np.zeros((self.feat_len, 5))
        self.finger_lengths = np.zeros((self.feat_len, 5))
        self.inner_distances = np.zeros((feat_len, 10))
        self.palm_direction = np.zeros((feat_len, 3))
        self.palm_radius = np.zeros((feat_len, 1))
        self.palm_grab = np.zeros((feat_len, 1))
        self.palm_pinch = np.zeros((feat_len, 1))
        # shape = reps, num of features + 1(for label)
        self.final_feat = np.zeros((reps, 27))

    def avg_and_append_features(self, curr_label, reps_completed):
        """
        Calculate the average of features for all frames and append it to the final feature list
        :param curr_label: Current label
        :type curr_label: int
        :param reps_completed: Number of repetitions of captured sets
        :type reps_completed: int
        """
        feat1 = np.mean(self.extended_fingers, axis=0)
        feat2 = np.mean(self.finger_lengths, axis=0)
        feat3 = np.mean(self.inner_distances,axis = 0)
        feat4 = np.mean(self.palm_direction, axis = 0)
        feat5 = np.mean(self.palm_radius, axis = 0)
        feat6 = np.mean(self.palm_grab, axis=0)
        feat7 = np.mean(self.palm_pinch, axis=0)
        self.final_feat[reps_completed][0] = curr_label
        self.final_feat[reps_completed][1:] = np.concatenate((feat1, feat2, feat3, feat4, feat5, feat6, feat7), axis=0)
