import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import numpy as np

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../Data/ModelData.csv")
print(data)

train, test = train_test_split(data, test_size=0.3)

decisionTreeClassifier = DecisionTreeClassifier(min_samples_split=100)
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

decisionTreeClassifier.fit(xTrain, yTrain)

yPrediction = decisionTreeClassifier.predict(xTest)
score = accuracy_score(yTest, yPrediction)*100 # closer to %100
f1Score = f1_score(yTest, yPrediction) # closer to 1
print("Accuracy using Decision Tree: {}. F1 score is {}".format(score, f1Score))
