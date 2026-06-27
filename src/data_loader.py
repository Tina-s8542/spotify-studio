import pandas as pd
from src.song import Song
import csv

class DataLoader :
    def __init__(self, path) :
        self.path = path
        self.songs = []
        
    def data_load(self) :
        self.songs = []
        try :
            datas = pd.read_csv(self.path)
        except FileNotFoundError :
            print("file not found.")
            return []
       
        for _, row in datas.iterrows() :
            song = Song(
                row["track_id"],
                row["artists"],
                row["album_name"],
                row["track_name"],
                row["popularity"],
                row["duration_ms"],
                row["energy"],
                row["explicit"],
                row["danceability"],
                row["key"],
                row["loudness"],
                row["mode"],
                row["speechiness"],
                row["acousticness"],
                row["instrumentalness"],
                row["liveness"],
                row["valence"],
                row["tempo"],
                row["time_signature"],
                row["track_genre"])

            self.songs.append(song)
        return self.songs

    def append_song(self, song) :
        with open(self.path, "a", newline = "", encoding = "utf-8") as f :
            writer = csv.writer(f)
            writer.writerow([
                song.track_id,
                song.artists,
                song.album_name,
                song.track_name,
                song.popularity,
                song.duration_ms,
                song.energy,
                song.explicit,
                song.danceability,
                song.key,
                song.loudness,
                song.mode,
                song.speechiness,
                song.acousticness,
                song.instrumentalness,
                song.liveness,
                song.valence,
                song.tempo,
                song.time_signature,
                song.track_genre])
            self.songs.append(song)
