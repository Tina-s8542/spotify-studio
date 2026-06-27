import pandas as pd
from src.data_loader import DataLoader
from src.song import Song
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
from src.data_cleaner import MeanImputer, MedianImputer, KNNImputer, IQROutlierHandler, ZScoreOutlierHandler
from src.song_suggestor import Suggestor
from src.data_modeler import SongPredictor

path = "data/spotify_tracks.csv"
loader = DataLoader(path)
df = None
original_df = None
predictor = None
#print(f"{len(songs)} songs loaded")
while True :
    print("\n------------------> Spotify Data Studio & Management System <------------------")
    print("\n\t1. Load Dataset & View Missing values Report ")
    print("\t2. Clean Missing Values (Mean / Median / KNN) ")
    print("\t3. Handle Outliers (IQR / Z-Score) ")
    print("\t4. Add a New Song to the Dataset (Interactive Input) ")
    print("\t5. Calculate Genre Insights & Correlation Matrix ")
    print("\t6. Generate Advanced Visualizations (Plots) ")
    print("\t7. Song Suggestor")
    print("\t8. Train Machine Learning Model")
    print("\t9. Predict Hit or Flop")
    print("\t0. Exit")
    print("----------------------------------------------------------------------------------")

    choice = input("\tEnter your choice : ")
    print()
    
    if choice == "1" :
        df = pd.read_csv(path)
        original_df = df.copy()
        print("\nDataset Loaded Successfully")
        print("\nMissing Values Report : \n")
        print(df.isnull().sum())

    elif choice == "2" :
        if df is None :
            print("Load dataset first!")
            continue
        print("\n1. Mean")
        print("2. Median")
        print("3. KNN")
        ch = input("Choose method : ")
        if ch == "1" :
            cleaner = MeanImputer()
            df = cleaner.impute(df)
            print("Mean Cleaning was Successful.")
        elif ch == "2" :
            cleaner = MedianImputer()
            df = cleaner.impute(df)
            print("Median Cleaning was Successful.")
        elif ch == "3" :
            cleaner = KNNImputer()
            df = cleaner.impute(df)
            print("KNN Cleaning was Successful.")
        else :
            print("Invalid choice!")
            continue

    elif choice == "3" :
        if df is None :
            print("Load dataset first!")
            continue
        print("\n1. IQR")
        print("2. Z-Score")
        ch = input("Choose method : ")
        if ch == "1" :
            h = IQROutlierHandler()
            df = h.handle(df)
            print("IQR Cleaning was Successful.")
        elif ch == "2" :
            h = ZScoreOutlierHandler()
            df = h.handle(df)
            print("Z-Score Cleaning was Successful.")
        else :
            print("Invalid choice!")
            continue

    elif choice == "4" :
        track_id = input("track_id : ")
        artists = input("artists : ")
        album_name = input("album_name : ")
        track_name = input("track_name : ")
        popularity = int(input("popularity (0-100) : "))
        track_genre = input("track_genre : ")

        song = Song(track_id,artists,album_name,track_name,popularity,0,0,False,0,0,0,0,0,0,0,0,0,0,0,track_genre)
        loader.append_song(song)
        print("Song added successfully.")

    elif choice == "5" :
        if df is None :
            print("Load dataset first!")
            continue
        analyz = DataAnalyzer(df)
        print("\nGenre Statistics : ")
        print(analyze.repetitionGenre())
        print("\nCorrelation Matrix : ")
        print(analyz.correlationMatrix())

    elif choice == "6" :
        if df is None :
            print("Load dataset first!")
            continue
        visualiz = DataVisualizer(df)
        print("\n1. Scatter Plot")
        print("2. Heatmap")
        print("3. BoxPlot Before")
        print("4. Boxplot After")
        print("5. Popularity Distribution")
        print("6. Energy Distribution")
        print("7. Genre Distribution")
        print("8. Energy & Popularity")

        ch = input("Choose Plot : ")
        if ch == "1" :
            visualiz.energyVsDanceability()
        elif ch == "2" :
            visualiz.heatmapPltCorr()
        elif ch == "3" :
            visualiz = DataVisualizer(original_df)
            visualiz.boxplotBefore()
        elif ch == "4" :
            visualiz.boxplotAfter(df)
        elif ch == "5" :
            visualiz.popularityPlt()
        elif ch == "6" :
            visualiz.energyPlt()
        elif ch == "7" :
            visualiz.genrePlt()
        elif ch == "8" :
            visualiz.energyVsPopularity()
        else :
            print("Invalid choice!")
            continue

    elif choice == "7" :
        if df is None :
            print("Load dataset first!")
            continue
        songName = input("Enter song name : ")
        try :
            t = int(input("Enter number of songs you want (1-10) : "))
        except ValueError :
            print("Please enter a valid number!")
            continue
        if not 1<= t <= 10  :
            print("Number must be between 1 and 10 !")
            continue

        songs = Suggestor(df).suggest(songName, t)
        if songs is None :
            print("Song not found!")
        else :
            print(songs)
    
    elif choice == "8" :
        if df is None :
            print("Load dataset first!")
            continue

        predictor = SongPredictor(df)
        predictor.train()

    elif choice == "9" :
        if predictor is None :
            print("Train model first!")
            continue

        energy = float(input("Enter energy : "))
        danceability = float(input("Enter danceability : "))
        acousticness = float(input("Enter acousticness : "))
        valence = float(input("Enter valence : "))

        result = predictor.prediction(energy, danceability, acousticness, valence)
        print(result)

    elif choice == "0" :
        print("You exited! Goodby.")
        exit()