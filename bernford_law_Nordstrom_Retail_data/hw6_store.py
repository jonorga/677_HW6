###
### CS667 Data Science with Python, Homework 6, Jon Organ
###

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


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

