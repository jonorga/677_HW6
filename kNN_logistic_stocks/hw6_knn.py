###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd
import math

file_cmg = pd.read_csv("cmg_weeks.csv")
file_spy = pd.read_csv("spy_weeks.csv")

def Q1ComputeData(df):
	k_vals = [3, 5, 7, 9, 11]
	results = []
	file_len = len(df.index)

	for k in k_vals:
		i = 0
		while i < file_len:
			nearest = []
			biggest = [-1, -1]

			j = 0
			while j < file_len:
				if j == i:
					j += 1
					continue
				cur_avg = df['Avg_Return'].get(i)
				cur_vol = df['Volatility'].get(i)
				oth_avg = df['Avg_Return'].get(j)
				oth_vol = df['Volatility'].get(j)
				distance = math.sqrt((abs(cur_avg - oth_avg) ** 2) + (abs(cur_vol - oth_vol) ** 2))

				if len(nearest) < k:
					if distance > biggest[0]:
						biggest = [distance, j]
					nearest.append([distance, j])
				#elif distance < biggest[0]:
				#	nearest.remove(biggest)
					# TODO: Label the new biggest one now, its not necessaryily the one you're adding

				# TODO: check distance here of i against j, 
				# 	if its one of k shortest distances, add to list
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