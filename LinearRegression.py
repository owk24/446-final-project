import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./Data/ModelData.csv")

train, test = train_test_split(data, test_size=0.2)

features = ["PERIOD", "MINUTES_REMAINING", "SHOT_TYPE", "SHOT_DISTANCE", "YEAR", "MONTH",
            "Back Court(BC)", "Center(C)", "Left Side Center(LC)", "Left Side(L)",
            "Right Side Center(RC)", "Right Side(R)",
            "Driving Layup Shot", "Jump Shot", "Layup Shot", "Pullup Jump shot", "Step Back Jump shot",
            "LOC_RATIO"]

target = ["SHOT_MADE_FLAG"]

# features = ["PERIOD", "MINUTES_REMAINING", "SECONDS_REMAINING", "SHOT_TYPE", "SHOT_DISTANCE", "YEAR", "MONTH", "DAY",
#             "Above the Break 3", "Backcourt", "In The Paint (Non-RA)", "Left Corner 3", "Mid-Range",
#             "Restricted Area", "Right Corner 3",
#             "Back Court(BC)", "Center(C)", "Left Side Center(LC)", "Left Side(L)",
#             "Right Side Center(RC)", "Right Side(R)",
#             "Driving Layup Shot", "Jump Shot", "Layup Shot", "Pullup Jump shot", "Step Back Jump shot",
#             "LOC_RATIO"]

xTrain = train[features]
yTrain = train[target]

xTest = test[features]
yTest = test[target]

logisticRegressor = LogisticRegression(max_iter=500)

logisticRegressor.fit(xTrain, yTrain.values.ravel())

yPrediction = logisticRegressor.predict(xTest)

print(classification_report(yTest, yPrediction))
print("The accuracy of the logistic model is: {}".format(accuracy_score(yTest, yPrediction)))

coefficientInfo = dict(zip(features, logisticRegressor.coef_.transpose().tolist()))
coefficientInfo["INTERCEPT"] = logisticRegressor.intercept_.tolist()
print(coefficientInfo)


