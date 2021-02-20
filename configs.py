import pandas as pd
from metrics import *
## configurations

# All metrics in SARIMA model
p_values = [0,1,2,3]
d_values = [2]
q_values = [0,1,2,3,4,5]
P_values = [0,1]
D_values = [7]
Q_values = [0,1]
m_values = [10]


# output_name is the name of csv table containing each combination of parameters and the error metrics
# we could select model by sorting this table on error metrics
output_name = "model_selection_rmse.csv"

# all metrics are defined in metrics.py, like RMSE, MAE, etc.
metrics_method = RMSE

# get the data we need
main_col = 'MedianSoldPrice_AllHomes.California'
df = pd.read_csv("data/df_train_one_col_split.csv", index_col=["Date"], parse_dates=["Date"])
data = df[main_col].values