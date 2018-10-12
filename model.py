from abc import ABC, abstractmethod

class model(ABC):
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
