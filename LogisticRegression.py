import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score, confusion_matrix

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

"""LOGISTIC MODEL IMPLEMENTATION"""
data = pd.read_csv("./Data/ModelDataRegression.csv")
# features = ["PERIOD", "MINUTES_REMAINING", "SECONDS_REMAINING", "SHOT_DISTANCE", "HOME", "MONTH",
#             "DAY", "3PT ATTEMPT",
#             "Above the Break 3", "Backcourt", "In The Paint (Non-RA)", "Left Corner 3",
#             "Mid-Range", "Restricted Area", "Right Corner 3",
#             "Back Court(BC)", "Center(C)", "Left Side Center(LC)",
#             "Left Side(L)", "Right Side Center(RC)", "Right Side(R)",
#             "Jump Shot", "Pullup Jump shot", "Driving Layup Shot", "Layup Shot", "Step Back Jump shot",
#             "Driving Floating Jump Shot", "Cutting Layup Shot", "Floating Jump shot", "Tip Layup Shot",
#             "Running Layup Shot", "Driving Finger Roll Layup Shot", "Hook Shot", "Fadeaway Jump Shot",
#             "Turnaround Jump Shot", "Cutting Dunk Shot", "Putback Layup Shot", "Turnaround Hook Shot",
#             "Turnaround Fadeaway shot", "Driving Floating Bank Jump Shot", "Dunk Shot",
#             "Driving Reverse Layup Shot", "Driving Dunk Shot", "Alley Oop Dunk Shot",
#             "Reverse Layup Shot", "Running Dunk Shot", "Driving Hook Shot", "Running Jump Shot",
#             "Alley Oop Layup shot", "Running Pull-Up Jump Shot", "Jump Bank Shot",
#             "Running Finger Roll Layup Shot", "Tip Dunk Shot", "Cutting Finger Roll Layup Shot",
#             "Turnaround Fadeaway Bank Jump Shot", "Finger Roll Layup Shot", "Putback Dunk Shot"]
train, test = train_test_split(data, test_size=0.40)

features = ["PERIOD",
            "HOME",
            "MONTH",
            "DAY",
            "LOC_X",
            "LOC_Y",
            "Back Court(BC)", "Center(C)", "Left Side Center(LC)",
            "Left Side(L)", "Right Side Center(RC)", "Right Side(R)",
            "Jump Shot", "Pullup Jump shot", "Driving Layup Shot", "Layup Shot", "Step Back Jump shot",
            "Driving Floating Jump Shot", "Cutting Layup Shot", "Floating Jump shot", "Tip Layup Shot",
            "Running Layup Shot", "Driving Finger Roll Layup Shot", "Hook Shot", "Fadeaway Jump Shot",
            "Turnaround Jump Shot", "Cutting Dunk Shot", "Putback Layup Shot", "Turnaround Hook Shot",
            "Turnaround Fadeaway shot", "Driving Floating Bank Jump Shot", "Dunk Shot",
            "Driving Reverse Layup Shot", "Driving Dunk Shot", "Alley Oop Dunk Shot",
            "Reverse Layup Shot", "Running Dunk Shot", "Driving Hook Shot", "Running Jump Shot",
            "Alley Oop Layup shot", "Running Pull-Up Jump Shot", "Jump Bank Shot",
            "Running Finger Roll Layup Shot", "Tip Dunk Shot", "Cutting Finger Roll Layup Shot",
            "Turnaround Fadeaway Bank Jump Shot", "Finger Roll Layup Shot", "Putback Dunk Shot"]

target = ["SHOT_MADE_FLAG"]

xTrain = train[features]
yTrain = train[target]
xTest = test[features]
yTest = test[target]

logisticRegressor = LogisticRegression(max_iter=500)
logisticRegressor.fit(xTrain, yTrain.values.ravel())

yPrediction = logisticRegressor.predict(xTest)

print(classification_report(yTest, yPrediction))
print("The accuracy of the logistic model is: {}%".format(accuracy_score(yTest, yPrediction) * 100))
print("The F1 score of the logistic model is: {}%".format(f1_score(yTest, yPrediction)))
print(confusion_matrix(yTest, yPrediction))

coefficientInfo = dict(zip(features, logisticRegressor.coef_.transpose().tolist()))
coefficientInfo["INTERCEPT"] = logisticRegressor.intercept_.tolist()
print(coefficientInfo)

'''FIND THE ACCURACY OF VARIOUS SHOTS'''
# accuracyDf = xTest
# accuracyDf["ACTUAL_SHOT_MADE"] = yTest
# accuracyDf["PRED_SHOT_MADE"] = yPrediction
# accuracyDf = accuracyDf.drop(["PERIOD", "HOME", "MONTH", "DAY", "LOC_X", "LOC_Y"], 1)
# shotEvents = ['Jump Shot', 'Pullup Jump shot', 'Driving Layup Shot', 'Layup Shot', 'Step Back Jump shot',
#               'Driving Floating Jump Shot', 'Cutting Layup Shot', 'Floating Jump shot', 'Tip Layup Shot',
#               'Running Layup Shot', 'Driving Finger Roll Layup Shot', 'Hook Shot', 'Fadeaway Jump Shot',
#               'Turnaround Jump Shot', 'Cutting Dunk Shot', 'Putback Layup Shot', 'Turnaround Hook Shot',
#               'Turnaround Fadeaway shot', 'Driving Floating Bank Jump Shot', 'Dunk Shot', 'Driving Reverse Layup Shot',
#               'Driving Dunk Shot', 'Alley Oop Dunk Shot', 'Reverse Layup Shot', 'Running Dunk Shot',
#               'Driving Hook Shot', 'Running Jump Shot', 'Alley Oop Layup shot', 'Running Pull-Up Jump Shot',
#               'Jump Bank Shot', 'Running Finger Roll Layup Shot', 'Tip Dunk Shot', 'Cutting Finger Roll Layup Shot',
#               'Turnaround Fadeaway Bank Jump Shot', 'Finger Roll Layup Shot', 'Putback Dunk Shot']
# numberShotCount = len(accuracyDf.index)
# actualShotAccuracyList = []
# predictShotAccuracyList = []
#
# def GetAccuracy(shot):
#     rowsOfInterest = accuracyDf.loc[accuracyDf[shot] == 1]
#     numberOfShotsTaken = len(rowsOfInterest.index)
#     numberActualShotsMade = len(rowsOfInterest[rowsOfInterest["ACTUAL_SHOT_MADE"] == 1])
#     numberPredictShotsMade = len(rowsOfInterest[rowsOfInterest["PRED_SHOT_MADE"] == 1])
#
#     return numberActualShotsMade, numberPredictShotsMade, numberOfShotsTaken
#
# for shot in shotEvents:
#     result = GetAccuracy(shot)
#     actualShotAccuracy = result[0] / result[2]
#     predictedShotAccuracy = result[1] / result[2]
#     actualShotAccuracyList.append(actualShotAccuracy)
#     predictShotAccuracyList.append(predictedShotAccuracy)
#
# resultsDf = pd.DataFrame([actualShotAccuracyList, predictShotAccuracyList],
#                          ["%_ACTUAL_SHOT_MADE", "%_PRED_SHOT_MADE"], shotEvents).transpose()
# resultsDf.to_csv("./LogShotAccuracy.csv", index=True, header=True)

'''MAKE A PLOT OF ACTUAL VS PREDICTED SHOTS'''
# redPatch = mpatches.Patch(color="Blue", label="Shot Went In")
# bluePatch = mpatches.Patch(color="Red", label="Shot Did Not Go in")
# plt.figure(figsize=(10, 7))
# plt.subplot(121)
# print(type(yPrediction))
# print(yPrediction)
# colorsPred = np.where(yPrediction == 1, "Blue", "Red")
# plt.title("Predicted Results from Test Dataset")
# plt.xlabel("LOC_X")
# plt.ylabel("LOC_Y")
# plt.legend(handles=[redPatch, bluePatch])
# plt.scatter(xTest.LOC_X, xTest.LOC_Y, color=colorsPred, s=4, alpha=0.5)
#
# plt.subplot(122)
# colorsTest = np.where(yTest["SHOT_MADE_FLAG"] == 1, "Blue", "Red")
# plt.title("Actual Results from Test Dataset")
# plt.xlabel("LOC_X")
# plt.ylabel("LOC_Y")
# plt.legend(handles=[redPatch, bluePatch])
# plt.scatter(xTest.LOC_X, xTest.LOC_Y, color=colorsTest, s=4, alpha=0.5)
# plt.show()
