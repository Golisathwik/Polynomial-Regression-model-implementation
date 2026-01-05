import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load the dataset from your local file
data= pd.read_csv('D:/sathwik files/ml practice/polynomial regression/predict.csv')
x= data[['Hours']].values
y= data['Marks'].values

# Initialize the PolynomialFeatures object
# degree=2 means we want to fit a curve (parabola), not a straight line
poly= PolynomialFeatures(degree=2)

# Convert the original 'x' data into polynomial features
# fit_transform() learns the pattern AND applies it to the training data
x_poly= poly.fit_transform(x)

# Initialize the Linear Regression model
lr_model=LinearRegression()

# Train the model
lr_model.fit(x_poly,y)

# Get user input for prediction
n=int(input("how many hours did you studied? "))
n_poly=poly.transform([[n]])

# Make a prediction based on the transformed input
predict_value= lr_model.predict(n_poly)
print(f"prediction for {n} hours is {int(predict_value[0])} marks.")

# --- Visualization ---

# Transform the original x values again to plot the blue line
x_poly_pred=poly.transform(x)
x_pred= lr_model.predict(x_poly_pred)
plt.scatter(x,y, color='red')
plt.plot(x, x_pred, color='blue')
plt.title('Polynomial Regression: Study Hours vs student Marks')
plt.xlabel('Study Hours')
plt.ylabel('Student Marks')
plt.show()