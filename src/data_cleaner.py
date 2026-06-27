from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer as skknn

class BaseImputer(ABC) :
    @abstractmethod
    def impute(self, data) :
        pass

class MeanImputer(BaseImputer) :
    def impute(self, data) :
        print("imputing by mean")
        return data.fillna(data.mean(numeric_only = True))

class MedianImputer(BaseImputer) :
    def impute(self, data) :
        print("imputing by median")
        return data.fillna(data.median(numeric_only = True))

class KNNImputer(BaseImputer) :
    def __init__(self, neighbors = 5) :
        self.model = skknn(n_neighbors = neighbors)

    def impute(self, data) :
        print("imputing by KNN")
        dataC = data.copy()
        cols = dataC.select_dtypes(include = [np.number]).columns
        dataC[cols] = self.model.fit_transform(dataC[cols])
        return dataC

class BaseOutlierHandler(ABC) :
    @abstractmethod
    def handle(self, data) :
        pass

class IQROutlierHandler(BaseOutlierHandler) :
    def handle(self, data) :
        print("handling by IQR")
        dataC = data.copy()
        cols = dataC.select_dtypes(include = [np.number]).columns

        for col in cols :
            q1 = dataC[col].quantile(0.25)
            q3 = dataC[col].quantile(0.75)
            IQR = q3 - q1

            lower = q1 - 1.5 * IQR
            upper = q3 + 1.5 * IQR

            dataC[col] = np.where(dataC[col] < lower, lower, 
                        np.where(dataC[col] > upper, upper, dataC[col]))
        return dataC

class ZScoreOutlierHandler(BaseOutlierHandler) :
    def handle(self, data) :
        print("handling by z-score")
        dataC = data.copy()
        cols = dataC.select_dtypes(include = [np.number]).columns

        for col in cols :
            mean = dataC[col].mean()
            std = dataC[col].std()
            if std == 0 :
                continue
            z = (dataC[col] - mean) / std
            dataC[col] = np.where(z>3, mean, np.where(z< -3, mean, dataC[col]))
        return dataC