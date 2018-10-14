from abc import ABC, abstractmethod


class Model(ABC):
    """
    Abstract class for a ML model.
    """

    @abstractmethod
    def train(self, training_data):
        """
        Trains the model with input training data set.
        """
        pass

    @abstractmethod
    def predict(self, input):
        """
        Uses trained model to predict response for an input.
        """
        pass

    @abstractmethod
    def validation(self):
        """
        Returns some measure of the accuracy of a trained model.
        """
        pass
