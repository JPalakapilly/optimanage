from abc import ABC, abstractmethod


class Workflow(ABC):
    """
    Abstract class for a workflow
    (Elastic tensor, bandgap computation, structure optimization, etc.)
    Each workflow type would be a separate subclass.
    Workflow instances must also include a mp-id.
    """

    @classmethod
    @abstractmethod
    def dependencies(cls):
        """
        Returns the workflow dependencies (other workflow classes)
        of this workflow

        Returns:
            dependencies (Set[Workflow])
        """
        pass

    def __init__(self, mp_id):
        """
        Args:
            mp_id (string): mp_id of the material for this workflow instance
        """
        self._mp_id = mp_id

    @property
    def mp_id(self):
        """
        The mp_id that this workflow corresponds to.
        """
        return self._mp_id

    def __eq__(self, other):
        """
        If two workflows are the same class and
        have the same mp-id then they are equal.
        """
        if type(other) == type(self):
            return self.mp_id() == other.mp_id()
        return False


class ElasticTensorWorkflow(Workflow):
    """
    Class for an elastic tensor computation workflow.
    """

    def __init__(self, mp_id):
        self._mp_id = mp_id
        self._mpquery_properties = set("elasticity.elastic_tensor")

    @classmethod
    def dependencies(cls):
        return None

    @property
    def mpquery_properties(self):
        return self._mpquery_properties
