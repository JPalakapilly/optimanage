from abc import abstractmethod, ABC


class Dispatcher(ABC):

    @abstractmethod
    def __init__(self):
        """
        Creates a new dispatcher.
        """
        pass

    @abstractmethod
    def update_objective(objective, weight):
        """
        Adds an objective to the dispatcher with an associated weight.
        If the objective is already in the dispatcher, update its weight.

        Args:
            objective (Objective): The objective to be added/update_dataset
            weight (int): The new weight of the objective
        """
        pass

    @abstractmethod
    def get_dataset_updates(self):
        """
        Check if dataset has changed and update as needed.
        """
        pass

    @abstractmethod
    def partition_data(objective):
        """
        Partition the dataset into a training set and a candidate set
        for a given objective based on needed workflows.
        Args:
            objective (Objective): The objective that is
                                   used to partition the dataset

        Returns:
            (training_set, candidate_set) (list(string),list(string)):
                    Two sets of mp_ids
        """
        pass

    @abstractmethod
    def run_objective(objective, candidates):
        """
        Uses an objective get 'scores' for candidates.
        Args:
            objective (Objective): The objective used to generate scores
            candidates (list): The materials that are to be scored

        Returns:
            scores (dict): Mapping of workflows to
                           scores for the input objective
        """
        pass

    @abstractmethod
    def rank_wflows(n):
        """
        Get a ranking of workflows given the current objectives and weights
        Args:
            n (int): The number of workflows to be returned in the ranking
        """
        pass
