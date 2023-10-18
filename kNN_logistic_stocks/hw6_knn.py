###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd
import matplotlib.pyplot as plt
import math

file_cmg = pd.read_csv("cmg_weeks.csv")
file_spy = pd.read_csv("spy_weeks.csv")

# Question 1 =================================================================================================
print("Question 1:")

def Q1ComputeData(df):
	k_vals = [3, 5, 7, 9, 11]
	results = []
	file_len = len(df.index)

	for k in k_vals:
		total_guess = 0
		correct_guess = 0
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
					nearest.sort()
				elif distance < biggest[0]:
					nearest.remove(biggest)
					nearest.append([distance, j])
					nearest.sort()
					biggest = nearest[-1]
				j += 1
			# Deal with nearest list here
			green_neighbor = 0
			red_neighbor = 0
			for neighbor in nearest:
				if df['Color'].get(neighbor[1]) == "Green":
					green_neighbor += 1
				elif df['Color'].get(neighbor[1]) == "Red":
					red_neighbor += 1
			if green_neighbor > red_neighbor:
				if df['Color'].get(i) == "Green":
					correct_guess += 1
			elif red_neighbor > green_neighbor:
				if df['Color'].get(i) == "Red":
					correct_guess += 1
			total_guess += 1
			i += 1
		results.append(correct_guess/total_guess)
	frame_data = [[3, results[0]], [5, results[1]], [7, results[2]], [9, results[3]], [11, results[4]]]
	results_frame = pd.DataFrame(frame_data, columns=['k_Value', 'k_Accuracy'])
	return results_frame


def Q1GenerateGraph(data):
	fig, ax = plt.subplots()
	ax.plot(data["k_Value"], data["k_Accuracy"])
	ax.set(xlabel='k Value', ylabel='k Accuracy',
	       title='k Accuracy by Value')
	ax.grid()
	print("Saving k Accuracy by Value graph...")
	fig.savefig("results/Q1_k_accuracy.png")

#print("Predicting values for " + file_name + " ....... ", end="\r", flush=True)

cmg_y1 = file_cmg[file_cmg['Week'] <= 50]
ans = Q1ComputeData(cmg_y1)
Q1GenerateGraph(ans)
print("The optimal value of k for year 1 is: " + str(ans['k_Value'].loc[ans['k_Accuracy'].idxmax()]))


print("\n")
# Question 2 =================================================================================================
print("Question 2:")

def Q2Accuracy(df, k_val):
	y_actu = []
	y_pred = []
	file_len = len(df.index)
	total_guess = 0
	correct_guess = 0
	i = 0
	while i < file_len:
		nearest = []
		biggest = [-1, -1]

		j = 0
		while j < file_len:
			if j == i:
				j += 1
				continue
			cur_avg = df['Avg_Return'].iloc[i]
			cur_vol = df['Volatility'].iloc[i]
			oth_avg = df['Avg_Return'].iloc[j]
			oth_vol = df['Volatility'].iloc[j]
			distance = math.sqrt((abs(cur_avg - oth_avg) ** 2) + (abs(cur_vol - oth_vol) ** 2))

			if len(nearest) < k_val:
				if distance > biggest[0]:
					biggest = [distance, j]
				nearest.append([distance, j])
				nearest.sort()
			elif distance < biggest[0]:
				nearest.remove(biggest)
				nearest.append([distance, j])
				nearest.sort()
				biggest = nearest[-1]
			j += 1
		# Deal with nearest list here
		green_neighbor = 0
		red_neighbor = 0
		for neighbor in nearest:
			if df['Color'].iloc[neighbor[1]] == "Green":
				green_neighbor += 1
			elif df['Color'].iloc[neighbor[1]] == "Red":
				red_neighbor += 1
		if green_neighbor > red_neighbor:
			predict = "Green"
			if df['Color'].iloc[i] == "Green":
				correct_guess += 1
		elif red_neighbor > green_neighbor:
			predict = "Red"
			if df['Color'].iloc[i] == "Red":
				correct_guess += 1
		total_guess += 1
		y_actu.append(df['Color'].iloc[i])
		y_pred.append(predict)
		i += 1
	print("Using the optimal k value of " + str(k_val) + " on year 2 gives an accuracy of "
		+ str(round((correct_guess/total_guess) * 100, 2)) + "%")
	return [y_actu, y_pred]


cmg_y2 = file_cmg[(file_cmg['Week'] > 50) & (file_cmg['Week'] <= 100)]
q3_data = Q2Accuracy(cmg_y2, ans['k_Value'].loc[ans['k_Accuracy'].idxmax()])


print("\n")
# Question 3 =================================================================================================
print("Question 3:")

y_actu = pd.Series(q3_data[0], name='Actual')
y_pred = pd.Series(q3_data[1], name='Predicted')
confusion_matrix = pd.crosstab(y_actu, y_pred)
print(confusion_matrix)




print("\n")
# Question 4 =================================================================================================
print("Question 4:")


