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