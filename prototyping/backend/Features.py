import numpy as np

class Features:
    def __init__(self, feat_len, reps):
        self.feat_len = feat_len
        self.extended_fingers = np.zeros((self.feat_len, 5))
        self.finger_lengths = np.zeros((self.feat_len, 5))
        self.inner_distances = np.zeros((feat_len, 10))
        self.final_feat = np.zeros((reps, 21))

    def avg_and_append_features(self, curr_label, reps_completed):
        feat1 = np.mean(self.extended_fingers, axis=0)
        feat2 = np.mean(self.finger_lengths, axis=0)
        feat3 = np.mean(self.inner_distances,axis = 0)
        self.final_feat[reps_completed][0] = curr_label
        self.final_feat[reps_completed][1:] = np.append(np.append(feat1,feat2),feat3)#np.append(feat1, feat2,)
