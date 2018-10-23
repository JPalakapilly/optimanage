from abc import abstractmethod, ABC


class Dispatcher(ABC):

    @abstractmethod
    def __init__(self, dataset=None):
        """
        Creates a new dispatcher.
        """
        self.dataset = dataset

    @property
    @abstractmethod
    def objective_training_data(self):
        """
        Mapping from objective to hash/serialization of the training data
        that was last used to train the objective's models.
        """
        pass

    @property
    @abstractmethod
    def dataset(self):
        """
        The dataset that this dispatcher interacts with. Typically a database.
        """
        pass

    @abstractmethod
    def add_objective(self, objective, weight):
        """
        Adds an objective to the dispatcher with an associated weight.
        If the objective is already in the dispatcher, update its weight.

        Args:
            objective (Objective): The objective to be added/update_dataset
            weight (int): The new weight of the objective
        """
        pass

    @abstractmethod
    def update(self):
        """
        Check if dataset has changed and update as needed.
        """
        pass

    @abstractmethod
    def partition_data(self, objective):
        """
        Partition the dataset into a training set and a candidate set
        for a given objective based on needed workflows.
        Args:
            objective (Objective): The objective that is
                                   used to partition the dataset

        Returns:
            (training_set, candidate_set) (List[string],List[string]):
                    A tuple containing two sets of mp_ids
        """
        pass

    @abstractmethod
    def run_objective(self, objective, candidates):
        """
        Uses an objective to get 'scores' for candidates.
        Args:
            objective (Objective): The objective used to generate scores
            candidates (List): The materials that are to be scored

        Returns:
            scores (Dict): Mapping of workflows to
                           scores for the input objective
        """
        pass

    @abstractmethod
    def rank_wflows(self, n):
        """
        Get a ranking of workflows given the current objectives and weights
        Args:
            n (int): The number of workflows to be returned in the ranking
        Returns:
            ranking (List(Workflow)): The top n workflows in the ranking.
        """
        pass
