###
### CS667 Data Science with Python, Homework 6, Jon Organ
###

import pandas as pd


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



