from abc import ABC, abstractmethod

class objective(ABC):

    @property
    @abstractmethod
    def wflows(self):
        """
        Returns a set of workflow types that are needed for this objective
        """
        pass

    @abstractmethod
    def store_model(self, store):
        """
        Serializes the model and stores somewhere
        """
        pass

    @abstractmethod
    def load_model(self, store):
        """
        Loads model from external store.
        """
        pass

    @abstractmethod
    def train_model(self, training_data):
        """
        Trains model given a set of training_data.
        """
        pass

    @abstractmethod
    def return_scores(self, design_space):
        """
        Returns a score for every material in the design_space
        """
        pass
