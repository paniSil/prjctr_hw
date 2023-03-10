import numpy as np
import math
import pandas as pd

# Create an an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
a = np.zeros((4, 3))
b = np.ones((4, 3))
c = np.arange(0, 12).reshape((4, 3))

# Tabulate the following function: F(x) = 2x^2 + 5, x in [1, 100] with step 1.
x = np.arange(1,101)
f_x = 2 * x**2 + 5

# Tabulate the following function: F(x) = e^-x, x in [-10, 10] with step 1.
x = np.arange(-10, 11)
f_xe = math.e**(-x)

# Import the dataset
data = pd.read_csv(r'scientist/Euro_2012.csv')

# Select only the Team, Yellow Cards and Red Cards columns.
data_c = data.loc[:, ['Team', 'Yellow Cards', 'Red Cards']]

# How many teams participated in the Euro2012?
howmany = data.shape[0]
print(howmany)

# Filter teams that scored more than 6 goals
filter_goals = data[data['Goals'] > 6]
print(filter_goals)
