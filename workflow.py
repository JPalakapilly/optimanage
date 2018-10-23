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
        self.mp_id = mp_id

    @property
    @abstractmethod
    def mp_id(self):
        """
        The mp_id that this workflow corresponds to.
        """"
        pass
