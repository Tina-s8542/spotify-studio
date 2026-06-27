import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

class SongPredictor :
    def __init__(self, data) :
        self.data = data
        self.model = None

    def train(self) :
        data = self.data.copy()
        data["label"] = (data["popularity"] > 50).astype(int) #Hit = 1 and Flop = 0

        x = data[["energy", "danceability", "acousticness", "valence"]]
        y = data["label"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)
        self.model = DecisionTreeClassifier()
        self.model.fit(x_train, y_train)
        print("Model trained successfully!")

    def prediction(self, energy, danceability, acousticness, valence) :
        if self.model is None :
            raise ValueError("Model is not trained yet!")
        
        result = self.model.predict([[energy, danceability, acousticness, valence]])
        if result[0] == 1 :
            return "Hit"
        return "Flop"
        
