from abc import abstractmethod, ABC

class dispatcher(ABC):

    @abstractmethod
    def add_objective(objective, weight):
        """
        Adds an objective to the dispatcher with an associated weight.
        If the objective is already in the dispatcher, update its weight.
        """
        pass

    @property
    @abstractmethod
    def dataset(self):
        """
        The dataset that this dispatcher interacts with.
        """
        pass

    @abstractmethod
    def update_dataset(self):
        """
        Update
        """
        pass

    @abstractmethod
    def partition_data(objective):
        """
        Partition the dataset into a training set and a "design space"
        for a given objective based on needed workflows.
        """
        pass

    @abstractmethod
    def run_objective(objective):
        """
        Uses an objective to train a model and get scores for candidates.
        """
        pass

    @abstractmethod
    def update_objectives():
        """
        Find which objectives need to be rerun after the dataset has changed, and rerun them.
        """
        pass

    @abstractmethod
    def rank_wflows():
        """
        Get a ranking of workflows given the current objectives and weights
        """
        pass
