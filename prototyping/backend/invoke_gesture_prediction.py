"""
Class to invoke update_service
"""
from gesture_prediction import UserGesturePrediction
from sklearn.externals import joblib


def main():
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')
    gp = UserGesturePrediction(model, scaler)
    gp.wait_for_connection()
    gp.extract_features()
    print gp.predicted_label

if __name__ == "__main__":
    main()
