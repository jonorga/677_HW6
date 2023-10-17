###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd

file_cmg = pd.read_csv("cmg_weeks.csv")
file_spy = pd.read_csv("spy_weeks.csv")

def Q1ComputeData(df):
	k_vals = [3, 5, 7, 9, 11]
	results = []
	file_len = len(df.index)

	for k in k_vals:
		i = 0
		while i < file_len:
			j = 0
			while j < file_len:
				if j == i:
					j += 1
					continue
				j += 1
			i += 1
	return results

# For each point
	# Calculate the distance to every other point
	# Keep the k closest points
	# Predicted color label is majority of other labels
	# Add counter to total checked
		# If correct color predicted, add to correct
	# Return

#print("Predicting values for " + file_name + " ....... ", end="\r", flush=True)

cmg_y1 = file_cmg[file_cmg['Week'] <= 50]
Q1ComputeData(cmg_y1)