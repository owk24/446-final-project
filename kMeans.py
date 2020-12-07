import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report, f1_score

import matplotlib.pyplot as plt
import seaborn as sns

""" Split player and team labels"""
data = pd.read_csv("./Data/ModelDataKMeans.csv")
columnNames = ['MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA',
              'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'PLAYER_NAME', 'TEAM_ABBREVIATION']
namesAndTeamsDf = data[["PLAYER_NAME", "TEAM_ABBREVIATION"]]
numericalData = data.drop(["PLAYER_NAME", "TEAM_ABBREVIATION"], 1)
dataFrameCol = columnNames[0:18]

stdScaler = StandardScaler()
stdNumData = stdScaler.fit_transform(numericalData)
""" Elbow plot to see which k value to select"""
# kMeansArgs = {
#     "init": "random",
#     "n_init": 10,
#     "max_iter": 300,
#     "random_state": 42,
#     }
#
# sseList = []
# for k in range(1, 15):
#     kmeans = KMeans(n_clusters=k, **kMeansArgs)
#     kmeans.fit(scaledNumericalData)
#     sseList.append(kmeans.inertia_)
#
# plt.plot(range(1, 15), sseList)
# plt.xticks(range(1, 15))
# plt.title("Elbow Plot")
# plt.xlabel("Number of clusters (k)")
# plt.ylabel("SSE")
# plt.show()

"""From the plot, roughly k= 3-4"""
kmeans = KMeans(n_clusters=3)
kmeans.fit(stdNumData)
yOutput = kmeans.predict(stdNumData)

yOutput = pd.DataFrame(yOutput)
yOutput = pd.concat([yOutput, namesAndTeamsDf], axis=1,ignore_index=True)
yOutput.columns = ["Value", "NAME", "TEAM"]


stdNumDataDf = pd.DataFrame(stdNumData)
stdNumDataDf = pd.concat([stdNumDataDf, namesAndTeamsDf], axis=1,ignore_index=True)
stdNumDataDf.columns = columnNames
# stdNumDataDf.to_csv("./kMeansOutput.csv", index=False, header=True)
centers = kmeans.cluster_centers_
"""TIME VS SCORE"""
# plt.title("Time played versus Score")
# plt.xlabel("Time played")
# plt.ylabel("Score")
# colorDict = {"LeBron James":"red", "Luka Doncic":"blue",
#              "JJ Reddick":"lawngreen", "Steven Adams":"violet"}
#              # Sorry I couldn't make this work, I was trying to show specific players as their own colors.
# plt.scatter(stdNumDataDf.MIN, stdNumDataDf.PTS, c=yOutput.Value, s=25, cmap="viridis")
# plt.scatter(centers[:, 0], centers[:, 16], c="black", s=200, alpha=0.5)

"""FG3A VS BLK"""
# plt.title("3-Point Attempts vs Blocks")
# plt.xlabel("3-Point Attempts")
# plt.ylabel("Blocks")
# print(stdNumDataDf)
# plt.scatter(stdNumDataDf.FG3A, stdNumDataDf.BLK, c=yOutput.Value, s=25, cmap="viridis")
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 4], centers[:, 12], c="black", s=200, alpha=0.5)

"""AST VS TOV"""
plt.title("Assists vs Turnovers")
plt.xlabel("Field Goal Attempts")
plt.ylabel("Turnovers")
print(stdNumDataDf)
plt.scatter(stdNumDataDf.AST, stdNumDataDf.TOV, c=yOutput.Value, s=25, cmap="viridis")
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 9], centers[:, 10], c="black", s=200, alpha=0.5)

plt.show()
