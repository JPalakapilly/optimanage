from abc import ABC, abstractmethod
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score
import numpy as np


class Model(ABC):
    """
    Abstract class for a ML model.
    """

    @abstractmethod
    def __init__(self):
        """
        Creates a model.
        """
        pass

    @abstractmethod
    def train(self, training_data):
        """
        Trains the model with input training data set.

        Args:
            training_data (List): list of inputs to train the model
        """
        pass

    @abstractmethod
    def predict(self, input):
        """
        Uses trained model to predict response for an input.

        Args:
            input: the input whose response needs to be predicted
        Returns:
            response: the predicted response of the model for input
        """
        pass

    @abstractmethod
    def validate(self, validation_data):
        """
        Returns some measure of the accuracy of a trained model.

        Args:
            validation_data: the data on which to run validation
                             (could be same as training data)
        Returns:
            accuracy (float): some measure of the predictivity of the model
        """
        pass


class RandomForestModel(Model):
    """

    """

    def __init__(self, max_depth=2, random_state=0, n_estimators=100):
        self._RFModel = RandomForestRegressor(max_depth=max_depth,
                                              random_state=random_state,
                                              n_estimators=n_estimators)
        # self._X = []
        # self._y = []

    def train(self, training_input, training_response):
        X = training_input
        y = training_response

        self._RFModel.fit(X, y)

    def predict(self, input):
        return self._RFModel.predict(input)

    def prediction_variance(self, input):
        predictions = []
        for decision_tree in self._RFModel.estimators_:
            predictions.append(decision_tree.predict(input))
        mean = sum(predictions)/len(predictions)
        squared_difs = [(p-mean)**2 for p in predictions]
        return sum(squared_difs)/len(squared_difs)

    def validate(self, validation_data):
        """
        Returns a dictionary containing r2 and RMSE values
        from cross-validation on using 10 folds.

        Args:
            validation_data: dataset to use for cross-validation
        """
        X = validation_data[0]
        y = validation_data[1]
        crossvalidation = KFold(n_splits=10, shuffle=False, random_state=1)
        r2_scores = cross_val_score(self._RFModel, X, y,
                                    scoring='r2', cv=crossvalidation,
                                    n_jobs=-1)
        scores = cross_val_score(self._RFModel, X, y,
                                 scoring='neg_mean_squared_error',
                                 cv=crossvalidation, n_jobs=-1)
        rmse_scores = [np.sqrt(abs(s)) for s in scores]

        return({"r2": np.mean(np.abs(r2_scores)),
                "RMSE": np.mean(np.abs(rmse_scores))})
