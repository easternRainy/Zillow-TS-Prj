#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")
from model_selection import *
from metrics import *
from configs import *


# In[45]:


model_selection = TimeSeriesModelSelection(data, metrics_method, p_values, d_values, q_values, P_values, D_values, Q_values, m_values)


# In[46]:


model_selection.fit()


# In[47]:


df = model_selection.get_result()
df.to_csv(output_name, index=False)

