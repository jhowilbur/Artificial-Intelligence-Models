"""
In this tutorial, we will train a linear regression model for predicting continuous values.

Any questions please contact us:
https://github.com/jhowilbur
https://www.linkedin.com/in/jwilbur
"""

from matplotlib import pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
from math import sqrt

# Create a dataset called 'df' that will load csv data
df = pd.read_csv("FuelConsumptionCo2.csv")

# VIEW THE DATAFRAME STRUCTURE
print (df.head())

"" "# Displays the Dataset summary" ""
print (df.describe())

"" "# Select only the Engine and CO2 features" ""
engines = df[['ENGINESIZE']]
co2 = df[['CO2EMISSIONS']]
print(engines.head())

"""
Divide the dataset into training data and test data
in this case we will use scikitlearn's train_test_split
"""

# In test_size the percentage that goes to training is defined
engines_training, engines_test, co2_training, co2_testing = train_test_split(engines, co2, test_size=0.2, random_state=42)
print(type(engines_training))

"" "#View the correlation between the features of the training dataset" ""
plt.scatter(engines_training, co2_training, color='blue')
plt.xlabel("Engine")
plt.ylabel("CO2 Emission")
plt.show()

"" "# We will train the linear regression model" ""

# CREATE A LINEAR REGRESSION TYPE MODEL
model = linear_model.LinearRegression()

# TRAINING THE MODEL USING THE TEST DATASET
# TO FIND THE VALUE OF A AND B (Y = A + B.X)
model.fit(engines_training, co2_training)

"" "#View the coefficients (A and B)" ""
# remembering that the intercept (value of A) is the value from where the line will start on the Y axis
print('(A) Intercept:', model.intercept_)
# and the value of (B) is the slope of this line (I know it's redundant but important to remember)
print('(B) Slope:', model.coef_)

"" "# We will display our regression line in the training dataset" ""
plt.scatter(engines_training, co2_training, color='blue')
# we apply the formula (Y = A + B.X)
plt.plot(engines_training, model.coef_[0][0] * engines_training + model.intercept_[0], '-r')
plt.ylabel("C02 emission")
plt.xlabel("Engines")
plt.show()

"" "# Let's run our model in the test dataset" ""

#First we have to make predictions using the model and test base
predicoesCo2 = model.predict(engines_training)

"" "# We will display our regression line in the test dataset" ""
plt.scatter(engines_training, co2_training, color='blue')
plt.plot(engines_test, model.coef_[0][0] * engines_test + model.intercept_[0], '-r')
plt.ylabel("C02 emission")
plt.xlabel("Engines")
plt.show()

"" "# We will evaluate the model" ""

#Now is showing the metrics
print("Sum of Errors squared (SSE):% .2f"% np.sum ((predicoesCo2 - co2_training) ** 2))
print("Mean Quadratic Error (MSE):% .2f"% mean_squared_error (co2_training, predicoesCo2))
print("Mean Absolute Error (MAE):% .2f"% mean_absolute_error (co2_training, predicoesCo2))
print("Root of the Mean Square Error (RMSE):% .2f"% sqrt (mean_squared_error (co2_training, predicoesCo2)))
print("R2-score:% .2f"% r2_score (co2_training, predicoesCo2))