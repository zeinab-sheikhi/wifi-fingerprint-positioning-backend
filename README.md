
# Multilayered Positioning System

This project implements a multilayered positioning system utilizing machine learning models for classification and regression. It provides RESTful API endpoints to handle fingerprint data and retrieve predicted positions based on input access points.

## Table of Contents
- [ML Models](#ml-models)
  - [Classification Model](#classification-model)
  - [Regression Model](#regression-model)
- [Database](#database)
  - [Configuration](#configuration)
  - [Database Management](#database-management)
- [API Endpoints](#api-endpoints)
  - [Point API](#point-api)
  - [Position API](#position-api)
- [Utilities](#utilities)
- [Application Structure](#application-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)

## ML Models

### Classification Model
The classification model is responsible for predicting the zone number based on the received access points data.

#### `classification.py`
```python
from util.feature_selection import open_joblib_file
from util.string_utils import StringUtils

classification_model = None

def load_classification_model():
    global classification_model
    classification_model = open_joblib_file(StringUtils.classification_model)

def classification_preds(X_test):
    preds = classification_model.predict(X_test).tolist()[0]
    return preds
```

### Regression Model
The regression model predicts the X and Y coordinates of the position based on the input data.

#### `regression.py`
```python
from util.feature_selection import open_joblib_file
from util.string_utils import StringUtils

regression_model = None

def load_regression_model():
    global regression_model
    regression_model = open_joblib_file(StringUtils.regression_model)

def regression_preds(X_test):
    preds = regression_model.predict(X_test).tolist()[0]
    return preds
```

## Database

### Configuration
This module manages the database configuration and connection setup using environment variables.

#### `config.py`
```python
import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Loads the environment variable file
load_dotenv()
...
```

### Database Management
This module handles database sessions and model initialization.

#### `db.py`
```python
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database.config import get_database

engine = get_database()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))                                        
Base = declarative_base()
...
```

## API Endpoints

### Point API
This API manages the storage of fingerprint data.

#### `point/routes.py`
```python
from flask import Blueprint, request
from flask_restful import Api, Resource

from models import Point, AccessPoint
from database.db import db_session

point_app = Blueprint('point_app', __name__, url_prefix='/api/v1/fingerprint')
api = Api(point_app)

class PointAPI(Resource):
    ...
api.add_resource(PointAPI, '/points')
```

### Position API
This API provides predictions for the position based on the provided access points.

#### `position/routes.py`
```python
from flask import Blueprint, request
from flask_restful import Api, Resource

from ml_models.classification import classification_preds
from ml_models.regression import regression_preds
from util.feature_selection import get_x_test

position_app = Blueprint('position_app', __name__, url_prefix='/api/v1/fingerprint')
api = Api(position_app)

class PositionAPI(Resource):
    ...
api.add_resource(PositionAPI, '/position')
```

## Utilities

### Data Handling
This module handles conversion between database tables and DataFrames.

#### `util/db_to_df.py`
```python
from datetime import datetime
import pandas as pd
from database.db import engine
from models import AccessPoint

def sql_table_to_df():    
    ...
```

### Feature Selection
This module manages the selection and processing of features for model input.

#### `util/feature_selection.py`
```python
import joblib
import numpy as np
from pathlib import Path

def open_joblib_file(file_path):
    ...
```

## Application Structure
The application is structured in the following way:
```
project_root/
├── app.py
├── config.py
├── database/
│   ├── config.py
│   └── db.py
├── ml_models/
│   ├── classification.py
│   └── regression.py
├── point/
│   └── routes.py
├── position/
│   └── routes.py
├── util/
│   ├── db_to_df.py
│   └── feature_selection.py
└── requirements.txt
```

## Requirements
To run this project, make sure you have the following dependencies installed:
```
Flask
Flask-RESTful
SQLAlchemy
python-dotenv
joblib
numpy
pandas
```

## Getting Started
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file based on the configuration provided in `config.py`.

4. Run the application:
   ```bash
   python manager.py
   ```

5. Access the APIs via `http://localhost:3000/api/v1/fingerprint`.
