from abc import ABC, abstractmethod


class Objective(ABC):
    """
    Abstract class for an objective for an optimization loop.
    """

    def __init__(self, model, wflows):
        """
        Creates an objective.
        """
        self.model = model
        self.wflows = wflows

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
        Serializes the model and stores in external store

        Args:
            store (Store): Location to store the model
        """
        pass

    @abstractmethod
    def load_model(self, store):
        """
        Loads model from external store.
        Args:
            store (Store): Location to load the model from
        """
        pass

    @abstractmethod
    def train_model(self, training_data):
        """
        Trains model given a set of training_data.
        Args:
            training_data (set(string)): MP-ids for the materials used to train
                                         the model
        """
        pass

    @abstractmethod
    def return_scores(self, candidates):
        """
        Returns a score for every material in the design_space.
        Stores this somewhere?

        Args:
            candidates (set(string)): MP-ids for materials to score

        Returns:
            scores (dict(Workflow:float)): mapping from workflow to score
        """
        pass
