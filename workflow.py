from abc import ABC, abstractmethod

class workflow(ABC):
    """
    Abstract class for a workflow
    (Elastic tensor computation, bandgap computation, structure optimization, etc.)
    """

    
    @classmethod
    @abstractmethod
    def dependencies(cls):
        """
        Returns the workflow dependencies (other workflows) of this workflow
        """
        pass
