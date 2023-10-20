###
### CS667 Data Science with Python, Homework 6, Jon Organ
###

import pandas as pd
# From year 1 of your stock, try to find the y = mx + b (looking for m and b values) of your stock
# Assign them randomly at first, then evaluate, take initial score, alter m and b values, re-evaluate
# if score improved, move farther in that direction, if not go in opposite direction, steps should be 
# proportional to change in the score
	# Start by adding to both m and b, if that keeps working keep going

# Evaluate process: Calculate the y value for the x (average return) input, if its greater than the
# observed y (volatility) value, then assign it to the green group, otherwise red group
	# green and red might have to be flipped here
# Check group assignments against actual groups, this is the resulting score
	# score = correct / total