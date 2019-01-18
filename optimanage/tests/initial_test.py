from optimanage import *


if __name__ == "__main__":

    dispatcher = MPDispatcher("toy_dataset3.json")

    rf_model = RandomForestModel()
    high_duc_obj = HighDuctilityObjective(rf_model, set([ElasticTensorWorkflow]))
    dispatcher.add_objective(high_duc_obj, 1.0)

    print(dispatcher._objective_partitioned_data)
    print(dispatcher._objective_weights)
    print(dispatcher.rank_wflows(10))
