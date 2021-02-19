import pandas as pd
from metrics import *
## configurations

# All metrics in SARIMA model
p_values = [3,4]
d_values = [1]
q_values = [0,1,2]
P_values = [0,1]
D_values = [0]
Q_values = [0,1]
m_values = [7]


# output_name is the name of csv table containing each combination of parameters and the error metrics
# we could select model by sorting this table on error metrics
output_name = "model_selection.csv"

# all metrics are defined in metrics.py, like RMSE, MAE, etc.
metrics_method = RMSE

# get the data we need
pharm_dt=pd.read_csv('pharm_history.csv',index_col='datum', parse_dates=True,squeeze=True)
data = pharm_dt['N05B'].values