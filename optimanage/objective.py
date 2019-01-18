from abc import ABC, abstractmethod
import numpy as np

class Objective(ABC):
    """
    Abstract class for an objective for an optimization loop.
    """

    def __init__(self, model, wflows):
        """
        Creates an objective.
        """
        self._model = model
        self._wflows = wflows
        self._objective_id = None

    @property
    def wflows(self):
        """
        Returns a set of workflow types that are needed for this objective
        """
        return self._wflows

    @property
    def objective_id(self):
        """
        Returns a unique id for this objective.
        """
        return self._objective_id


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
    def return_scores(self, candidates):
        """
        Returns a score for every material in the design_space.
        Stores this somewhere?

        Args:
            candidates (Set[string]): MP-ids for materials to score

        Returns:
            scores (Dict[string:float]): mapping from MP-ids to scores
        """
        pass


class HighDuctilityObjective(Objective):
    """
    Toy example of objective looking for materials with high ductility.
    Ductility is modeled using Pugh's ratio: K/G

    """

    def __init__(self, model=None, wflows=None):
        self._model = model
        self._wflows = wflows
        self._objective_id = "HighDuctilityObjective"

    def model_input_property_names(self):
        return set(["elasticity.G_Voigt"])

    def model_response_property_names(self):
        return set(["elasticity.K_VRH"])

    def return_scores(self, candidates):
        print(candidates)
        scores = []
        candidates.rewind()
        for candidate in candidates:
            input_row = []
            for input_prop in self.model_input_property_names():
                input_row.append(self.nested_dict_search(candidate, input_prop))
        #    print(input_row)
            scores.append((candidate, self.score(self._model.predict(np.array(input_row).reshape(-1, 1)),
                                      self._model.prediction_variance(np.array(input_row).reshape(-1, 1)))))
        return scores

    def score(self, prediction, uncertainty):
        return prediction

    def train_model(self, training_data):
        training_input = []
        training_response = []
        training_data.rewind()
        for data in training_data:
            input_row = []
            response_row = []
            for input_prop in self.model_input_property_names():
                input_row.append(self.nested_dict_search(data, input_prop))
                training_input.append(input_row)
            for response_prop in self.model_response_property_names():
                response_row.append(self.nested_dict_search(data, response_prop))
                training_response.append(response_row)
        training_input = np.array(training_input)
        training_response = np.array(training_response)
        self._model.train(training_input, training_response)

    @staticmethod
    def nested_dict_search(obj, ref):
        while "." in ref:
            subobject = ref.split(".", 1)[0]
            ref = ref.split(".", 1)[1]
            obj = obj[subobject]
        return obj[ref]

    def load_model(self, store):
        pass

    def store_model(self, store):
        pass
