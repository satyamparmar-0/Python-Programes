# Linear Regression Tutorial

## 1. What is Linear Regression?
Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The goal is to find the best-fitting line, represented mathematically by the formula:

    y = β0 + β1*x1 + β2*x2 + ... + βn*xn + ε

Where:
- **y** is the dependent variable (output)
- **β0** is the intercept
- **β1, β2, ..., βn** are the coefficients (weights)
- **x1, x2, ..., xn** are the independent variables (features)
- **ε** is the error term

## 2. Generating a Synthetic Dataset
We start by creating a synthetic dataset using NumPy:

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # For reproducibility
X = 2 * np.random.rand(100, 1)  # 100 random points in [0, 2]
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Synthetic Dataset')
plt.show()
```

## 3. Implementing Linear Regression from Scratch with Gradient Descent
To implement linear regression using gradient descent, we compute the gradients and update the parameters:

```python
def predict(X, theta):
    return X.dot(theta)

def compute_cost(X, y, theta):
    m = len(y)
    return (1/(2*m)) * np.sum(np.square(predict(X, theta) - y))

def gradient_descent(X, y, theta, learning_rate=0.01, iterations=1000):
    m = len(y)
    cost_history = np.zeros(iterations)

    for i in range(iterations):
        theta -= (1/m) * (X.T.dot(predict(X, theta) - y)) * learning_rate
        cost_history[i] = compute_cost(X, y, theta)

    return theta, cost_history

# Prepare data
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add bias term (intercept)

# Initial parameter vector
theta_initial = np.random.randn(2, 1)

# Run gradient descent
theta_best, cost_history = gradient_descent(X_b, y, theta_initial)
```

## 4. Implementing Linear Regression with Scikit-learn
Scikit-learn makes it easier. Here's how you can use it:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.scatter(X, y)
plt.plot(X, y_pred, color='red')  # Line of best fit
plt.title('Linear Regression with Scikit-learn')
plt.show()
```

## 5. Evaluation Metrics: MSE, RMSE, R²
We can evaluate our model using several metrics:

```python
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
print(f'R²: {r2}')
```

## 6. Plotting Results using Matplotlib
Already covered in previous sections, but you can customize further:

```python
plt.figure(figsize=(10,6))
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Result')
plt.legend()
plt.show()
```
