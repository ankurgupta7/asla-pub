import os
import sys
root_path = os.path.dirname(os.path.abspath('../..'))
sys.path.append(root_path)

import unittest
import numpy as np
from ...ml_tools.predict_service import PredictService


class TestPredictService(unittest.TestCase):

    def test_predict_label(self):
        cur_dir = os.path.dirname(__file__)
        model_file = os.path.join(cur_dir, 'model.pkl')
        scaler_file = os.path.join(cur_dir, 'scaler.pkl')
        predict_service = PredictService(model_file, scaler_file)
        # Dummy data to predict
        predict_service.to_predict = np.asarray([[5.000,1.000,1.000,1.000,1.000,1.000,0.912,0.952,0.999,0.950,0.871,113.552,147.522,160.465,173.213,42.299,67.464,102.324,28.618,69.522,42.090,-0.064,0.408,-0.910,355.084,0.000,0.000]])
        label = predict_service.predict_label()[0]
        assert label is not None
