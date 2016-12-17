import os
import sys
root_path = os.path.dirname(os.path.abspath('../..'))
sys.path.append(root_path)

import unittest
os.environ["NOQT"] = "1"

from ...ml_tools.training_service import TrainingService


class TestTrainService(unittest.TestCase):
    def test_send_to_server(self):
        training_service = TrainingService()
        training_service.data_collected.append([1.0,0.0,0.0,0.0,0.0,0.0,0.64405988898939126,0.43286370429485993,0.44834133700421908,0.41235343308661099,0.3469668740008871,0.34371233289868103,0.40828497280713716,0.4433201085482209,0.48035387845879773,0.066284041578365288,0.12990745855314656,0.19961350351175433,0.087854278969364541,0.16832708601553587,0.090744482113904776,2.2580298568323398,1.1450696130708649,0.6864718099738798,0.67575605336230593,1.1724271550882008,0.91631425088687979,0.94012758527416695,0.95528917031228322,0.99649583828187149,0.24437468738163726,0.49015454368030925,0.7164206131660209,0.25163106922048367,0.48480930001938044,0.2364486647012729,0.7464669314954987,0.72442173433487289,0.66810782239963651,0.6118602906310936,0.60397581443122372,0.41130367963352743,0.46973571300486061,0.59517009120652165,0.69099427809895086,0.13137286499741244,0.31236898875482477,0.47306505686919675,0.18834839023541097,0.35004843543634201,0.17057448011294188,0.61028499254541457,0.53112407339347545,0.52499141422773477,0.48559522419255313,0.43034533525151747,0.19089377991199621,0.27466794249569498,0.36712991964429792,0.45962800062118125,0.084823496178930063,0.18801814936749536,0.29599126382154595,0.12299810525271543,0.23903738173316341,0.1249233550217851,135.55982142901712,139.50262155194054,131.90465423242128,125.40478667104867,12.971992068275361,23.508027478030119,39.35083759397299,12.376187409899156,27.610576334130037,15.954685199453094,61.11252422600495,75.356573820232953,78.65848363295575,73.211254090614261,73.766846437138824,0.12294904422014952,0.93345548212528229,-0.33599089831113815,35.116945266723633,1.0,0.36383325979113579,-0.072531899437308311,-0.32905722409486771,-0.94122043251991272,0.0,0.0,0.0,-4.0419702529907227,-6.6193227767944336,0.58221811056137085,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
        sent = training_service.send_to_server()
        assert sent is True