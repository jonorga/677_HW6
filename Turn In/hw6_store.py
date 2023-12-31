###
### CS667 Data Science with Python, Homework 6, Jon Organ
###

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import PercentFormatter


# Question 1 =======================================================================================
print("Question 1:")
df = pd.read_csv("nordstrom_product_data.csv", low_memory=False)
print("Product data file read...")


print("\n")
# Question 2 =======================================================================================
print("Question 2:")
print("There are", df['CATEGORY'].nunique(), "categories in the file")


print("\n")
# Question 3 =======================================================================================
print("Question 3:")
highest_val = 0
highest_name = ""
lowest_val = 100
lowest_name = ""
for cat in df.CATEGORY.unique():
	temp_df = df[df['CATEGORY'] == cat]
	if temp_df['SUBCATEGORY'].nunique() > highest_val:
		highest_val = temp_df['SUBCATEGORY'].nunique()
		highest_name = cat
	if temp_df['SUBCATEGORY'].nunique() < lowest_val:
		lowest_val = temp_df['SUBCATEGORY'].nunique()
		lowest_name = cat

print(highest_name + " has the most subcategories (" + str(highest_val) + "), and "
	+ lowest_name + " has the least subcategories (" + str(lowest_val) + ")")


print("\n")
# Question 4 =======================================================================================
print("Question 4:")
for cat in df.CATEGORY.unique():
	temp_df = df[df['CATEGORY'] == cat]
	print("Category: " + cat + ", median price: $" + str(temp_df['PRICE_RETAIL'].median())
		+ ", average price: $" + str(round(temp_df['PRICE_RETAIL'].mean(), 2)))



print("\n")
# Question 5 =======================================================================================
print("Question 5:")
df['First'] = (df['PRICE_RETAIL']).astype(str).str.replace('.', '').str[:1].astype(int)
df['Second'] = (df['PRICE_RETAIL']).astype(str).str.replace('.', '').str[1:2].astype(int)
df['Third'] = (df['PRICE_RETAIL']).astype(str).str.replace('.', '').str[2:3].replace('', '0').astype(int)


def Q5Hist(col, num):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.hist(df[col], bins = num, histtype='bar', ec="black", color="red")
	ax.set_title("Histogram of " + col + " digit")
	ax.set_xlabel(col + " Digit")
	ax.set_ylabel("Frequency")
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	print("Saving " + col + " histogram...")
	fig.savefig("Q5_" + col + "_Hist.png")

Q5Hist('First', df['First'].nunique())
Q5Hist('Second', df['Second'].nunique())
Q5Hist('Third', df['Third'].nunique())



print("\n")
# Question 6 =======================================================================================
print("Question 6:")
first_perc = []
second_perc = []
third_perc = []
for i in range(9):
	perc1 = df['First'][df['First'] == i + 1].count() / df['First'].count()
	perc2 = df['Second'][df['Second'] == i + 1].count() / df['Second'].count()
	perc3 = df['Third'][df['Third'] == i + 1].count() / df['Third'].count()
	first_perc.append(perc1)
	second_perc.append(perc2)
	third_perc.append(perc3)

i = 0
first_1_err = []
second_1_err = []
third_1_err = []

def Q6GenData2(input_data):
	output = []
	output.append( abs(input_data[0] - 0.301) )
	output.append( abs(input_data[1] - 0.176) )
	output.append( abs(input_data[2] - 0.125) )
	output.append( abs(input_data[3] - 0.097) )
	output.append( abs(input_data[4] - 0.079) )
	output.append( abs(input_data[5] - 0.067) )
	output.append( abs(input_data[6] - 0.058) )
	output.append( abs(input_data[7] - 0.051) )
	output.append( abs(input_data[8] - 0.046) )
	return output
first_2_err = Q6GenData2(first_perc)
second_2_err = Q6GenData2(second_perc)
third_2_err = Q6GenData2(third_perc)

while i < 9:
	error1 = abs(first_perc[i] - 0.11)
	error2 = abs(second_perc[i] - 0.11)
	error3 = abs(third_perc[i] - 0.11)
	first_1_err.append(error1)
	second_1_err.append(error2)
	third_1_err.append(error3)
	i += 1


def Q6GenerateData(input_data):
	output = []
	i = 0
	count = 0
	stage = input_data[0]
	while i < 1000:
		if i / 1000 > stage:
			if count == 8:
				i = 1000
			else:
				count += 1
				stage += input_data[count]		
		else:
			output.append(count + 1)
		i += 1
	return output

first_1_err_d = Q6GenerateData(first_1_err)
second_1_err_d = Q6GenerateData(second_1_err)
third_1_err_d = Q6GenerateData(third_1_err)
first_2_err_d = Q6GenerateData(first_2_err)
second_2_err_d = Q6GenerateData(second_2_err)
third_2_err_d = Q6GenerateData(third_2_err)



def Q6GenerateHist(data, model, digit):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.hist(data, bins = 9, histtype='bar', ec="black", weights=np.ones(len(data)) / len(data))
	ax.set_title("Error histogram of " + model + " " + digit + " digit")
	ax.set_xlabel(digit + " Digit")
	ax.set_ylabel("Frequency")
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
	print("Saving " + model + " " + digit + " error histogram...")
	fig.savefig("Q6_" + model + "_" + digit + "_Hist.png")

Q6GenerateHist(first_1_err_d, "Model_1", "first")
Q6GenerateHist(second_1_err_d, "Model_1", "second")
Q6GenerateHist(third_1_err_d, "Model_1", "third")
Q6GenerateHist(first_2_err_d, "Model_2", "first")
Q6GenerateHist(second_2_err_d, "Model_2", "second")
Q6GenerateHist(third_2_err_d, "Model_2", "third")



print("\n")
# Question 7 =======================================================================================
print("Question 7:")


def Q7ComputeRMSE(data):
	rmse_result = 0
	for val in data:
		rmse_result += (val ** 2)
	rmse_result /= len(data)
	return math.sqrt(rmse_result)

first_1_rmse = Q7ComputeRMSE(first_1_err)
second_1_rmse = Q7ComputeRMSE(second_1_err)
third_1_rmse = Q7ComputeRMSE(third_1_err)
first_2_rmse = Q7ComputeRMSE(first_2_err)
second_2_rmse = Q7ComputeRMSE(second_2_err)
third_2_rmse = Q7ComputeRMSE(third_2_err)


if first_1_rmse < first_2_rmse:
	first_result = "1"
else:
	first_result = "2"
print("For the first digit, the " + first_result + " Model was closer to real distribution"
	+ "\nModel 1 RMSE: " + str(first_1_rmse) + "\nModel 2 RMSE: " + str(first_2_rmse))

if second_1_rmse < second_2_rmse:
	second_result = "1"
else:
	second_result = "2"
print("For the first digit, the " + second_result + " Model was closer to real distribution"
	+ "\nModel 1 RMSE: " + str(second_1_rmse) + "\nModel 2 RMSE: " + str(second_2_rmse))

if third_1_rmse < third_2_rmse:
	third_result = "1"
else:
	third_result = "2"
print("For the first digit, the " + third_result + " Model was closer to real distribution"
	+ "\nModel 1 RMSE: " + str(third_1_rmse) + "\nModel 2 RMSE: " + str(third_2_rmse))



print("\n")
# Question 8 =======================================================================================
print("Question 8:")
# Categories: Clothing, Shoes, Handbags

def Q8GenPerc(cat):
	first_perc = []
	second_perc = []
	third_perc = []
	for i in range(9):
		perc1 = df['First'][(df['First'] == i + 1) & (df['CATEGORY'] == cat)].count() / df['First'][df['CATEGORY'] == cat].count()
		perc2 = df['Second'][(df['Second'] == i + 1) & (df['CATEGORY'] == cat)].count() / df['Second'][df['CATEGORY'] == cat].count()
		perc3 = df['Third'][(df['Third'] == i + 1) & (df['CATEGORY'] == cat)].count() / df['Third'][df['CATEGORY'] == cat].count()
		first_perc.append(perc1)
		second_perc.append(perc2)
		third_perc.append(perc3)
	return first_perc, second_perc, third_perc

c_first_perc, c_second_perc, c_third_perc = Q8GenPerc("Clothing")
s_first_perc, s_second_perc, s_third_perc = Q8GenPerc("Shoes")
h_first_perc, h_second_perc, h_third_perc = Q8GenPerc("Handbags")



def Q8GenErr1(data1, data2, data3):
	i = 0
	output1 = []
	output2 = []
	output3 = []
	while i < 9:
		error1 = abs(data1[i] - 0.11)
		error2 = abs(data2[i] - 0.11)
		error3 = abs(data3[i] - 0.11)
		output1.append(error1)
		output2.append(error2)
		output3.append(error3)
		i += 1
	return output1, output2, output3

c_first_1_err, c_second_1_err, c_third_1_err = Q8GenErr1(c_first_perc, c_second_perc, c_third_perc)
s_first_1_err, s_second_1_err, s_third_1_err = Q8GenErr1(s_first_perc, s_second_perc, s_third_perc)
h_first_1_err, h_second_1_err, h_third_1_err = Q8GenErr1(h_first_perc, h_second_perc, h_third_perc)


c_first_2_err = Q6GenData2(c_first_perc)
c_second_2_err = Q6GenData2(c_second_perc)
c_third_2_err = Q6GenData2(c_third_perc)

s_first_2_err = Q6GenData2(s_first_perc)
s_second_2_err = Q6GenData2(s_second_perc)
s_third_2_err = Q6GenData2(s_third_perc)

h_first_2_err = Q6GenData2(h_first_perc)
h_second_2_err = Q6GenData2(h_second_perc)
h_third_2_err = Q6GenData2(h_third_perc)



c_first_1_rmse = Q7ComputeRMSE(c_first_1_err)
c_second_1_rmse = Q7ComputeRMSE(c_second_1_err)
c_third_1_rmse = Q7ComputeRMSE(c_third_1_err)
c_first_2_rmse = Q7ComputeRMSE(c_first_2_err)
c_second_2_rmse = Q7ComputeRMSE(c_second_2_err)
c_third_2_rmse = Q7ComputeRMSE(c_third_2_err)


s_first_1_rmse = Q7ComputeRMSE(s_first_1_err)
s_second_1_rmse = Q7ComputeRMSE(s_second_1_err)
s_third_1_rmse = Q7ComputeRMSE(s_third_1_err)
s_first_2_rmse = Q7ComputeRMSE(s_first_2_err)
s_second_2_rmse = Q7ComputeRMSE(s_second_2_err)
s_third_2_rmse = Q7ComputeRMSE(s_third_2_err)


h_first_1_rmse = Q7ComputeRMSE(h_first_1_err)
h_second_1_rmse = Q7ComputeRMSE(h_second_1_err)
h_third_1_rmse = Q7ComputeRMSE(h_third_1_err)
h_first_2_rmse = Q7ComputeRMSE(h_first_2_err)
h_second_2_rmse = Q7ComputeRMSE(h_second_2_err)
h_third_2_rmse = Q7ComputeRMSE(h_third_2_err)

print("For the first digit:")
if c_first_1_rmse < s_first_1_rmse and c_first_1_rmse < h_first_1_rmse:
	print("The Clothing category was the closest to equal weight P")
elif s_first_1_rmse < c_first_1_rmse and s_first_1_rmse < h_first_1_rmse:
	print("The Shoes category was the closest to equal weight P")
elif h_first_1_rmse < c_first_1_rmse and h_first_1_rmse < s_first_1_rmse:
	print("The Handbags category was the closest to equal weight P")


print("For the second digit:")
if c_second_1_rmse < s_second_1_rmse and c_second_1_rmse < h_second_1_rmse:
	print("The Clothing category was the closest to equal weight P")
elif s_second_1_rmse < c_second_1_rmse and s_second_1_rmse < h_second_1_rmse:
	print("The Shoes category was the closest to equal weight P")
elif h_second_1_rmse < c_second_1_rmse and h_second_1_rmse < s_second_1_rmse:
	print("The Handbags category was the closest to equal weight P")


print("For the third digit:")
if c_third_1_rmse < s_third_1_rmse and c_third_1_rmse < h_third_1_rmse:
	print("The Clothing category was the closest to equal weight P")
elif s_third_1_rmse < c_third_1_rmse and s_third_1_rmse < h_third_1_rmse:
	print("The Shoes category was the closest to equal weight P")
elif h_third_1_rmse < c_third_1_rmse and h_third_1_rmse < s_third_1_rmse:
	print("The Handbags category was the closest to equal weight P")



print("\n")
# Question 9 =======================================================================================
print("Question 9:")
print("For both models it seems they were most accurate with the third digit. The second digit for"
	+ "\nboth models also seem to be decently inaccurate concerning the 4 through 7. The first model"
	+ "\nwas very far off in terms of the distribution of ones in the first digit place.")








