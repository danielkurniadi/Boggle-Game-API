# How to code here

## Module structure

The following are service layer responsibility/scope

- libs --> business logic
- data_access --> layer access mysql or another microservice
- views --> facing client
- models --> define database/orm model here

## Service Layer Responsbility

### `model` (inside models)
Define your model and attribute here, quite straight forward

Name of the file: 

`__object_name_models.py`

### `model_manager` module (inside data_access)
the only manager that can access model, define the number models manager accordingly

Name of the file:

`__object_name__model_manager.py`

### `manager` module (inside libs)
manager is the layer that deal with the business logic.
manager can accessed multiple models manager

Name of the file:

`__object_name__manager.py`

Notes that: when manager needs other manager meaning that 
there is a possibility that we can create another new manager that will
call your old manager together with the dependent manager of old manager

From:
```
Manager A ----- Manager B
```
To:
```
New Manager -----
|               |
|               |
Manager A    Manager B
```

We called this kind of manager is `constructing manager`

## `view` (inside views)

API layer or also known as HTTP Router, can only passed whatever the attribute that the payload have
to the manager that takes care the business logic

Name of the file
`__object_name__views.py`
