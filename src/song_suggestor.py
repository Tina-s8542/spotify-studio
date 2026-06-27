import pandas as pd

class Suggestor :
    def __init__(self, data) :
        self.data = data

    def suggest(self, track_name, top = 3) :
        song = self.data[self.data["track_name"] == track_name]
        if song.empty :
            return "There isn't this song!"

        genre = song.iloc[0]["track_genre"]
        findSomeGenre = self.data[self.data["track_genre"] == genre]
        findSomeGenre = findSomeGenre[findSomeGenre["track_name"] != track_name]

        findSomeGenre = findSomeGenre.sort_values(by= "popularity", ascending= False)

        return findSomeGenre[["track_name", "artists", "popularity"]].head(top)
