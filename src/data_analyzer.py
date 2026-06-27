import pandas as pd

class DataAnalyzer :
    def __init__(self, data) :
        self.data = data

    def getSummary(self) :
        return self.data.describe()

    def popularSongs(self, n = 10) :
        return self.data.nlargest(n, "popularity")[["track_name", "artists", "popularity"]]

    def repetitionGenre(self) :
        return self.data["track_genre"].value_counts()

    def correlationMatrix(self) :
        return self.data.corr(numeric_only = True)