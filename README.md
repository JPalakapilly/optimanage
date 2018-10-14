#Optimanage
Optimanage is an interface to manage optimization loops. Very early stages.
(Oct 2018)

## Motivation
MP has a limited amount of computational time on supercomputing clusters. MP is constantly running computationally expensive workflows on supercomputing clusters (Elastic tensor calculations, band structure estimations, structure optimization etc.). Often, the

There also exists a way for users to "vote" for new elastic tensor calculations using

## Classes
Objectives represent an optimization goal. (Maximize ductility).
  Generally, this goal is expected to be a max, min, or target function of one response variable.
  Objectives have associated workflows

Models are used to predict responses for an input material. These are expected to be ML models that need training data.

Dispatchers manage several objectives that interact with the same dataset. The dataset will likely be in the form of a database that the dispatcher can query. The dispatcher should be able to check for updates in the database and also write to the database. The dispatcher will ask for scores for each candidate from its objectives, weight these scores

Objectives will be able to use model(s) to predict a "score" for an input material.

Workflows are computationally expensive workflows that generally result in further information about a material.
##Examples

```
high_duc_obj = new HighDuctilityObjective()
negative_poisson_obj = new NegativePoissonObjective()
dispatcher = new Dispatcher()
dispatcher.add(high_duc_obj)
dispatcher.add(negative_poisson_obj)

```
