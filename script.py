import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
housing_data = pd.read_csv('housing_data.csv')
# print(housing_data.head())
X = housing_data[['Sq ft', 'Burglaries']]
y = housing_data['Rent']

# Create the model
reg = LinearRegression()

# Train the model
reg.fit(X, y)

square_footage = 2800
number_of_burglaries = 1

y_pred = reg.predict(np.array([square_footage, number_of_burglaries]).reshape(1, 2))

print(y_pred)