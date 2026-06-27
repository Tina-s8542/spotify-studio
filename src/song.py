class Song() :
    def __init__(self, track_id, artists, album_name, track_name, popularity,
                duration_ms, energy, explicit, danceability, key, loudness, mode, speechiness, acousticness,
                instrumentalness, liveness, valence, tempo, time_signature, track_genre) :

        self.track_id = track_id
        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name
        self.popularity = popularity
        self.duration_ms = duration_ms
        self.energy = energy
        self.explicit = explicit
        self.danceability = danceability
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.time_signature = time_signature
        self.track_genre = track_genre

    @property
    def popularity(self) :
        return self._popularity 
    @popularity.setter
    def popularity(self, value) :
        if not 0 <= value <= 100 :
            raise ValueError("popularity must be between 0 and 100!")
        self._popularity = value
    
    @property
    def energy(self) :
        return self._energy
    @energy.setter
    def energy(self, value) :
        if not 0 <= value <= 1 :
            raise ValueError("energy must be between 0 and 1!")
        self._energy = value

    @property
    def danceability(self):
        return self._danceability
    @danceability.setter
    def danceability(self, value):
        if not 0 <= value <= 1:
            raise ValueError("danceability must be between 0 and 1!")
        self._danceability = value

    @property
    def speechiness(self):
        return self._speechiness
    @speechiness.setter
    def speechiness(self, value):
        if not 0 <= value <= 1:
            raise ValueError("speechiness must be between 0 and 1!")
        self._speechiness = value

    @property
    def acousticness(self):
        return self._acousticness
    @acousticness.setter
    def acousticness(self, value):
        if not 0 <= value <= 1:
            raise ValueError("acousticness must be between 0 and 1!")
        self._acousticness = value

    @property
    def instrumentalness(self):
        return self._instrumentalness
    @instrumentalness.setter
    def instrumentalness(self, value):
        if not 0 <= value <= 1:
            raise ValueError("instrumentalness must be between 0 and 1!")
        self._instrumentalness = value

    @property
    def liveness(self):
        return self._liveness
    @liveness.setter
    def liveness(self, value):
        if not 0 <= value <= 1:
            raise ValueError("liveness must be between 0 and 1!")
        self._liveness = value

    @property
    def valence(self):
        return self._valence
    @valence.setter
    def valence(self, value):
        if not 0 <= value <= 1:
            raise ValueError("valence must be between 0 and 1!")
        self._valence = value

    def __str__(self) :
        return f"{self.track_name} - {self.artists}"