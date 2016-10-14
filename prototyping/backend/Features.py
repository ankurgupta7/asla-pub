import numpy as np

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

    def get_finger_lengths(self):
        return self.filger_lengths