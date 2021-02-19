# Time Series Analysis Final Project
## How to generate report from Jupyter Notebook
[Voila](https://voila.readthedocs.io/en/stable/install.html) is a great tool to turn Jupyter Notebook into an independent web app. To install Voila, run 

```
conda install -c conda-forge voila
```

We use the following command to turn a notebook into web app, removing the code, leaving only the markdown and output plots.

```
voila PATH/TO/NOTEBOOK.ipynb
```

Now we can see the clean version of notebook in our browser, we simply print the webpage and save it as PDF! We do not need to write a separate report.

## How to use Model Selection

We create a grid search script for model selection. Taking SARIMA for example, the script will evaluate the model for each combination of parameters in parallel. So it won't take much long.

First, we need to modify config.py file, changing the parameters in it. The details are in config.py file.

Second, we need to run `select_model_by_config.py`

```
python3 select_model_by_config.py
```

This script will generate a csv file containing the results.