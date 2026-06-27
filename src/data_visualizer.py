import matplotlib.pyplot as plt
import seaborn as sn

class DataVisualizer :
    def __init__(self, data) :
        self.data = data

    def energyVsDanceability(self) :
        plt.figure(figsize = (8,6))
        plt.scatter(self.data["danceability"], self.data["energy"], alpha = 0.2)
        plt.title("Danceability vs Energy")
        plt.xlabel("danceability")
        plt.ylabel("energy")
        plt.show()

    def heatmapPltCorr(self) :
        corr = self.data.corr(numeric_only = True)
        plt.figure(figsize= (12,8))
        sn.heatmap(corr, annot = True, cmap = "coolwarm")
        plt.title("correlation Matrix")
        plt.show()

    def boxplotBefore(self) :
        plt.figure(figsize = (6,5))
        plt.boxplot(self.data["popularity"])
        plt.title("Popularity before cleaning")
        plt.show()

    def boxplotAfter(self, dataClean) :
        plt.figure(figsize = (6,5))
        plt.boxplot(dataClean["popularity"])
        plt.title("Popularity after cleaning")
        plt.show()

    def popularityPlt(self) :
        self.data["popularity"].hist(bins = 30)
        plt.title("popularity distribution")
        plt.xlabel("popularity")
        plt.ylabel("count")
        plt.show()

    def energyPlt(self) :
        self.data["energy"].hist(bins = 30)
        plt.title("energy distribution")
        plt.xlabel("energy")
        plt.ylabel("count")
        plt.show()

    def genrePlt(self) :
        self.data["track_genre"].value_counts().head(12).plot(kind = "bar")
        plt.title("number of genres")
        plt.show()

    def energyVsPopularity(self) :
        plt.scatter(self.data["energy"], self.data["popularity"])
        plt.title("energy vs popularity")
        plt.xlabel("energy")
        plt.ylabel("popularity")
        plt.show()
