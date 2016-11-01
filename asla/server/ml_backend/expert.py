from profile import Profile
from binary.ml_tools.training_service import TrainingService


class Expert(Profile):
    """
    Inherits Profile
    """
    def __init__(self):
        Profile.__init__(self)
        self.admin_token = None
        self.training_service = TrainingService()

    def start_training_service(self, label):
        """
        Invokes the training service after the expert has selected a label
        """
        self.training_service = TrainingService()
        self.training_service.capture_gesture(label)

    def end_training_service(self):
        """
        Ends gesture collection.
        """
        self.training_service.send_to_server()