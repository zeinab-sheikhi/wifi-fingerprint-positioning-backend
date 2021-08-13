import joblib
import pickle
import os

import numpy as np
from pathlib import Path

from util.string_utils import StringUtils

def open_pkl_file(file_path):

    base_path = Path(__file__).parent
    file_path = (base_path / file_path).resolve()
    if os.path.exists(file_path):
        file = pickle.load(open(file_path, 'rb'))
    else:
        print('No File with this Name, check File Name')
        file = None
    return file

def open_joblib_file(file_path):
    base_path = Path(__file__).parent
    file_path = (base_path / file_path).resolve()
    if os.path.exists(file_path):
        file = joblib.load(open(file_path, 'rb'))
    else:
        print('No File with this Name, check File Name')
        file = None
    return file

def get_x_test(accessPoints):
    
    trained_columns = open_joblib_file(StringUtils.columns_path)
    test_columns = list(accessPoints.keys())

    # remove extra APs that were detected during online phase, but were not used for training the model
    accessPoints = drop_columns(trained_columns, test_columns, accessPoints)

    # add APs that were used for training the model, 
    # but were not detected during online phase and perform imputation on them       

    # accessPoints = mean_imputation(trained_columns, test_columns, accessPoints)
    # accessPoints = min_imputation(trained_columns, test_columns, accessPoints)
    accessPoints = zero_imputation(trained_columns, test_columns, accessPoints)

    rssi_list = list(dict(sorted(accessPoints.items())).values())
    X_test = np.array(rssi_list).reshape(1, -1)
    return X_test

def drop_columns(trained_columns, test_columns, accessPoints):

    for column in test_columns:
        if column not in trained_columns:
            accessPoints.pop(column)
    return accessPoints        
    
def mean_imputation(trained_columns, test_columns, accessPoints):
    dict_of_mean = {
    '0e:bf:a0:39:f3:00': -83.0,
    '1a:19:d6:4b:55:2b': -86.0,
    '1c:15:1f:9c:62:84': -89.0,
    '1c:49:7b:e4:8c:cf': -86.0,
    '1c:5f:2b:ff:a8:ac': -87.0,
    '2e:96:6c:50:53:64': -91.0,
    '30:f7:72:49:54:e3': -89.0,
    '48:5a:b6:4d:d9:4b': -88.0,
    '52:02:91:dd:68:33': -90.0,
    '52:42:e5:00:65:cc': -89.0,
    '5a:0e:85:e9:be:31': -80.0,
    '60:38:e0:dc:de:e5': -89.0,
    '6e:48:95:16:b9:1f': -91.0,
    '82:6b:06:12:78:4a': -91.0,
    '94:2d:dc:f2:48:82': -88.0,
    '9a:2c:a5:27:08:e0': -89.0,
    'a6:c9:f7:b2:03:59': -89.0,
    'be:dd:c2:9f:39:91': -90.0,
    'c4:e9:84:b3:99:fd': -86.0,
    'd8:38:0d:02:a4:01': -90.0,
    'd8:38:0d:02:a5:61': -87.0,
    'd8:38:0d:02:a5:81': -90.0,
    'd8:38:0d:02:a5:a1': -70.0,
    'd8:38:0d:02:b0:41': -74.0,
    'd8:38:0d:02:b0:61': -89.0,
    'd8:38:0d:02:b0:81': -81.0,
    'd8:38:0d:02:b3:c1': -88.0,
    'd8:38:0d:02:b3:e1': -90.0,
    'd8:38:0d:02:b4:01': -87.0,
    'd8:38:0d:02:b7:a1': -83.0,
    'd8:38:0d:02:b7:c1': -88.0,
    'd8:38:0d:02:b7:e1': -88.0,
    'd8:38:0d:02:b8:01': -84.0,
    'd8:38:0d:a0:1a:91': -70.0,
    'd8:fe:e3:16:06:f4': -91.0,
    'e8:50:8b:aa:1a:58': -85.0,
    'ec:9b:f3:74:12:f9': -85.0,
    'f4:ec:38:f0:92:b2': -88.0,
    'f4:f2:6d:ee:a0:c4': -90.0,
    'fe:f5:c4:ad:64:85': -90.0}

    for column in trained_columns:
        if column not in test_columns:
            accessPoints[column] = dict_of_mean[column]
    return accessPoints        

def min_imputation(trained_columns, test_columns, accessPoints):
    dict_of_min = {
    '0e:bf:a0:39:f3:00': -88.0,
    '1a:19:d6:4b:55:2b': -90.0,
    '1c:15:1f:9c:62:84': -93.0,
    '1c:49:7b:e4:8c:cf': -93.0,
    '1c:5f:2b:ff:a8:ac': -95.0,
    '2e:96:6c:50:53:64': -91.0,
    '30:f7:72:49:54:e3': -89.0,
    '48:5a:b6:4d:d9:4b': -92.0,
    '52:02:91:dd:68:33': -94.0,
    '52:42:e5:00:65:cc': -89.0,
    '5a:0e:85:e9:be:31': -89.0,
    '60:38:e0:dc:de:e5': -89.0,
    '6e:48:95:16:b9:1f': -92.0,
    '82:6b:06:12:78:4a': -94.0,
    '94:2d:dc:f2:48:82': -93.0,
    '9a:2c:a5:27:08:e0': -93.0,
    'a6:c9:f7:b2:03:59': -94.0,
    'be:dd:c2:9f:39:91': -95.0,
    'c4:e9:84:b3:99:fd': -91.0,
    'd8:38:0d:02:a4:01': -94.0,
    'd8:38:0d:02:a5:61': -95.0,
    'd8:38:0d:02:a5:81': -94.0,
    'd8:38:0d:02:a5:a1': -92.0,
    'd8:38:0d:02:b0:41': -92.0,
    'd8:38:0d:02:b0:61': -93.0,
    'd8:38:0d:02:b0:81': -93.0,
    'd8:38:0d:02:b3:c1': -93.0,
    'd8:38:0d:02:b3:e1': -95.0,
    'd8:38:0d:02:b4:01': -94.0,
    'd8:38:0d:02:b7:a1': -93.0,
    'd8:38:0d:02:b7:c1': -93.0,
    'd8:38:0d:02:b7:e1': -94.0,
    'd8:38:0d:02:b8:01': -93.0,
    'd8:38:0d:a0:1a:91': -88.0,
    'd8:fe:e3:16:06:f4': -94.0,
    'e8:50:8b:aa:1a:58': -91.0,
    'ec:9b:f3:74:12:f9': -91.0,
    'f4:ec:38:f0:92:b2': -88.0,
    'f4:f2:6d:ee:a0:c4': -94.0,
    'fe:f5:c4:ad:64:85': -94.0}  

    for column in trained_columns:
        if column not in test_columns:
            accessPoints[column] = dict_of_min[column]
    return accessPoints          

def zero_imputation(trained_columns, test_columns, accessPoints):

    for column in trained_columns:
        if column not in test_columns:
            accessPoints[column] = 0
    return accessPoints        
