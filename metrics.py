from sklearn.metrics import mean_squared_error
from math import sqrt

def RMSE(test_data, predictions):
    return sqrt(mean_squared_error(test_data, predictions))

def MAE(test_data, predictions):
    return mean_absolute_error(test_data, predictions)
