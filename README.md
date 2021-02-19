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