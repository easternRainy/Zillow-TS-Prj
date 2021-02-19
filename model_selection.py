from threading import Thread
import statsmodels.api as sm
import itertools
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class Worker(Thread):
    '''
    inner class for parallel computing, each worker only is in charge of a combination
    of parameters
    '''

    def __init__(self, data, combination, metrics, train_rate):
        Thread.__init__(self)
        self.data = data
        self.combination = combination
        self.metrics = metrics
        self.train_rate = train_rate

    def run(self):
        '''
        fit one model using a combination
        '''
        print(f"Unit test: {self.combination}")
        p, d, q, P, D, Q, m = self.combination
        trend_order = (p, d, q)
        seasonal_order = (P, D, Q, m)

        # train test split
        n = len(self.data)
        train_size = int(n * self.train_rate)
        train, test = self.data[0:train_size], self.data[train_size:]

        history = [x for x in train]
        predictions = list()
        for t in range(len(test)):
            model = sm.tsa.statespace.SARIMAX(history, order=trend_order,seasonal_order=seasonal_order)
            res = model.fit()

            yhat = res.predict(start=len(history), end=len(history))
            predictions.append(yhat) #store prediction
            history.append(test[t]) #store observation

        error_metrics = self.metrics(test, predictions)

        self.error_metrics = error_metrics

    def get_error_metrics(self):
        try:
            return self.error_metrics
        except:
            return -1



class TimeSeriesModelSelection:
    """
    This is a class to grid-search for best time series SARIMA models
    
    data: np.array() time series
    metrics: MAE, RMSE, AIC, BIC, or user defined.
    train_rate: for train_test split
    p, q, ..., m are model parameters
    """
    def __init__(self, 
                 data, 
                 metrics,
                 p_vals=[0], 
                 d_vals=[0], 
                 q_vals=[0],
                 P_vals=[0],
                 D_vals=[0],
                 Q_vals=[0],
                 m_vals=[0],
                 train_rate=0.8,):
    
        self.data = data
        self.metrics = metrics
        self.train_rate = train_rate
        
        self.p_vals = p_vals
        self.d_vals = d_vals
        self.q_vals = q_vals
        self.P_vals = P_vals
        self.D_vals = D_vals
        self.Q_vals = Q_vals
        self.m_vals = m_vals
        
        self.combinations = list(itertools.product(*[p_vals, d_vals, q_vals, \
                                                     P_vals, D_vals, Q_vals, \
                                                     m_vals]))
        
    def fit(self):
        
        threads = []
        for combination in self.combinations:
            worker = Worker(self.data, combination, self.metrics, self.train_rate)
            worker.start()
            threads.append(worker)
            
        for worker in threads:
            worker.join()
        
        results = [worker.get_error_metrics() for worker in threads]
        self.df = pd.DataFrame(columns=['p', 'd', 'q', 'P', 'D', 'Q', 'm'], data=self.combinations)
        self.df['error_metrics'] = results
        
        
    
    def get_result(self):
        return self.df
            
    
