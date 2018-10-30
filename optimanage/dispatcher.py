from abc import abstractmethod, ABC
from maggma.stores import JSONStore
from objective import Objective


class Dispatcher(ABC):

    @abstractmethod
    def __init__(self, dataset=None):
        """
        Creates a new dispatcher.
        """
        self._dataset = dataset
        self._objective_partitioned_data = {}
        self._objective_weights = {}

    @property
    def objective_partitioned_data(self):
        """
        Mapping from objective to hash/serialization of the training data
        that was last used to train the objective's models.
        """
        return self._objective_partitioned_data

    @property
    def dataset(self):
        """
        The dataset that this dispatcher interacts with. Typically a database.
        """
        return self._dataset

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


class MPDispatcher(Dispatcher):
    """
    Dispatcher to use with Materials Project data. Reads from a JSON file.
    """

    def __init__(data_file_path):
        """
        Assumers that the data_file_path contains data from
        a mpquery request in JSON format.
        """
        self._dataset = JSONStore(data_file_path)
        self._objective_partitioned_data = {}
        self._weights

    def add_objective(self, objective, weight):
        assert isinstance(objective, Objective)
        assert isinstance(weight, float)

        self._objective_weights[objective] = weight
        self._objective_partitioned_data[objective] = \
            self.partition_data(objective)

    def partition_data(objective):
        training_input_props = list(objective.model_training_property_names())
        response_props = list(objective.model_response_property_names())
        training_criteria = {}
        candidate_critera = {}

        for prop in training_props:
            training_criteria[prop] = {"$exists": 1}
            candidate_critera[prop] = {"$exists": 1}
        for prop in response_props:
            training_criteria[prop] = {"$exists": 1}
            candidate_critera[prop] = {"$exists": 0}

        training_data = self._dataset.query(criteria=training_criteria,
                                            properties=)
        candidate_data = self._dataset.query(criteria=candidate_criteria,
                                             properties=training_props)
        return (training_data, candidate_data)
