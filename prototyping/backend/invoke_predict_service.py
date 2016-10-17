"""
Class to invoke update_service
"""
from predict_service import PredictService


def main():
    predict_service = PredictService()
    predict_service.capture_gesture()
    print predict_service.predict_label()

if __name__ == "__main__":
    main()
