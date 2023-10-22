###
### CS667 Data Science with Python, Homework 6, Jon Organ
###

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing

file = pd.read_csv("cmg_weeks.csv")

returns = file["Avg_Return"][file['Week'] <= 50].to_numpy().reshape(-1, 1)
color = file["Color"][file['Week'] <= 50].to_numpy()

returns2 = file["Avg_Return"][(file['Week'] > 50) & (file['Week'] <= 100)].to_numpy().reshape(-1, 1)
color2 = file["Color"][(file['Week'] > 50) & (file['Week'] <= 100)].to_numpy()


model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(returns, color)


# Question 1 ==========================================================================================
print("Question 1:")
print("The logistic regression classifier found the following coefficients:")
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)




print("\n")
# Question 2 ==========================================================================================
print("Question 2:")
print("Using year 1 as training data, the accuracy for year 2 is " + str(model.score(returns2, color2)))




print("\n")
# Question 3 ==========================================================================================
print("Question 3:")
print(confusion_matrix(color2, model.predict(returns2)))



print("\n")
# Question 4 ==========================================================================================
print("Question 4:")
print("The True Positive Rate is 1, the True Negative Rate is 0")



print("\n")
# Question 5 ==========================================================================================
print("Question 5:")



