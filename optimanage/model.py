from abc import ABC, abstractmethod


class Model(ABC):
    """
    Abstract class for a ML model.
    """

    @abstractmethod
    def __init__(self):
        """
        Creates a model.
        """
        pass

    @abstractmethod
    def train(self, training_data):
        """
        Trains the model with input training data set.

        Args:
            training_data (List): list of inputs to train the model
        """
        pass

    @abstractmethod
    def predict(self, input):
        """
        Uses trained model to predict response for an input.

        Args:
            input: the input whose response needs to be predicted
        Returns:
            response: the predicted response of the model for input
        """
        pass

    @abstractmethod
    def validate(self):
        """
        Returns some measure of the accuracy of a trained model.

        Returns:
            accuracy (float): some measure of the predictivity of the model
        """
        pass


class RandomForestModel(Model):
    """

    """
