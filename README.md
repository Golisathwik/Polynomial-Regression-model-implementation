# Polynomial-Regression-model-implementation
Polynomial Regression is a statistical method used to model a relationship between a dependent variable y and an independent variable x as an n^th degree polynomial. Unlike linear regression, which fits a straight line, polynomial regression fits a curve to the data points.

---

# 📈 Polynomial Regression (Non-Linear Data)

While Linear Regression fits a straight line, **Polynomial Regression** is used when the data shows a curve or non-linear pattern. It models the relationship between the independent variable ($x$) and dependent variable ($y$) as an $n$-th degree polynomial.

### 🔹 Mathematical Model
For a polynomial of degree $n$, the equation becomes:

$$y = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3 + \dots + \beta_n x^n$$

Where:
* $\beta_0$: The Intercept.
* $\beta_1, \beta_2, \dots$: The Coefficients for each power of $x$.
* $n$: The Degree (1 = Line, 2 = Parabola/Curve, 3 = S-shape).

<img width="816" height="445" alt="Image" src="https://github.com/user-attachments/assets/d004bdfb-7521-46fa-86c8-6691b766a449" />

## 🧠 Understanding Degrees: The "Bends" Analogy
In Polynomial Regression, the **Degree** ($n$) determines the flexibility of the model. A simple way to visualize this is to think of the degree as the number of **"bends"** the line is allowed to make.

### 1. The Differences in "Bends"
| Degree | Shape | Bends | Description |
| :--- | :--- | :---: | :--- |
| **1 (Linear)** | Straight Line | **0** | A rigid straight line. It can only go up or down at a constant rate. |
| **2 (Quadratic)** | Parabola (U-Shape) | **1** | It can change direction once (e.g., go up then down, like a ball thrown in the air). |
| **3 (Cubic)** | S-Shape | **2** | It can change direction twice (e.g., go up, then down, then back up). |
| **$n$ (High)** | Wavy / Complex | **$n-1$** | A very wiggly line that can twist and turn as many times as needed. |

---

### 2. When do we use which?
The goal of Machine Learning is **not** to connect every single dot. The goal is to find the *general pattern* so we can predict new data accurately.

#### ✅ Use Degree 2 (Quadratic)
Best when the data has a simple curve or a single peak/valley.
* **Example:** *Fuel Efficiency vs. Speed.* (Efficiency goes up as you speed up, peaks at 60mph, then drops as you go faster).

#### ✅ Use Degree 3 or 4 (Cubic/Quartic)
Best when the pattern is more complex with multiple fluctuations.
* **Example:** *Electricity Usage over a Day.* (Low at night, high in the morning, dips in the afternoon, high again in the evening).

#### ❌ Use Degree $n$ (High Complexity)
**Almost Never.**

> **⚠️ The Danger of High Degrees (Overfitting)**
> Imagine a model with **Degree 20**. It has **19 bends** available. It is so flexible that it will wiggle frantically to pass through every single data point perfectly.
>
> While it gets 100% accuracy on the training data, it fails miserably on new data because it learned the "noise" instead of the actual pattern. This is called **Overfitting**.

---

## 🧮 Solved Example: Degree 2 (Quadratic)
**Objective:** Find the best-fit curve for the following data points which follow a non-linear trend.

**Data Points:** $(1, 1), (2, 4), (3, 9), (4, 15)$

Since the data curves upwards, we use a **Quadratic Equation (Degree 2):**
$$y = a_0 + a_1 x + a_2 x^2$$

### Step 1: The Calculation Table
To solve for the coefficients ($a_0, a_1, a_2$), we calculate the sums ($\Sigma$) of the powers of $x$ and $y$.

| $x$ | $y$ | $xy$ | $x^2$ | $x^2y$ | $x^3$ | $x^4$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 4 | 8 | 4 | 16 | 8 | 16 |
| 3 | 9 | 27 | 9 | 81 | 27 | 81 |
| 4 | 15 | 60 | 16 | 240 | 64 | 256 |
| **Sum ($\Sigma$)** | **29** | **96** | **30** | **338** | **100** | **354** |

### Step 2: The Normal Equations (Matrix Form)

We arrange these sums into the matrix equation $X \cdot A = B$ to solve for the unknown coefficients ($A$).

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}n&\sum%20x_i&\sum%20x_i^2\\\sum%20x_i&\sum%20x_i^2&\sum%20x_i^3\\\sum%20x_i^2&\sum%20x_i^3&\sum%20x_i^4\end{bmatrix}\cdot\begin{bmatrix}a_0\\a_1\\a_2\end{bmatrix}=\begin{bmatrix}\sum%20y_i\\\sum%20x_i%20y_i\\\sum%20x_i^2%20y_i\end{bmatrix}" alt="Normal Equation Matrix Formula" />
</p>

Substituting the values from our table ($n=4$):

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}4&10&30\\10&30&100\\30&100&354\end{bmatrix}\cdot\begin{bmatrix}a_0\\a_1\\a_2\end{bmatrix}=\begin{bmatrix}29\\96\\338\end{bmatrix}" alt="Normal Equation Matrix Substituted Values" />
</p>

### Step 3: Final Model Solution
By solving the matrix equation (calculating $X^{-1} \cdot B$), we get the optimal values:

$$
\begin{bmatrix} a_0 \\ a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} -0.75 \\ 0.95 \\ 0.75 \end{bmatrix}
$$

**The Final Best-Fit Equation:**
$$y = -0.75 + 0.95x + 0.75x^2$$

---

## How to Run the Model
Follow these steps to set up the environment and run the Polynomial Regression model on your local machine.

### 1. Prerequisites
Ensure you have Python installed. You will need the following libraries:
```
pip install pandas matplotlib scikit-learn

```

### 2. Project Structure

Keep both files in the same directory:

* `polynomial_regression.py` (The main logic)
* `predict.csv` (The training dataset)

### 3. Execution

Open your terminal or command prompt, navigate to the folder, and run:

```
python polynomial_regression.py

```

### 4. Interactive Prediction

Once the script runs, it will ask for input:

1. **Enter Size:** The program will prompt you to enter a house size (e.g., `2500`).
2. **Output:** It will display the predicted price in the console.
3. **Visualization:** A graph will pop up showing the data points and the regression curve.

---

## 🛠️ Development Logic: Step-by-Step

Here is the breakdown of how the `polynomial_regression.py` script was developed to transform a linear model into a polynomial one.

### Step 1: Data Loading & Preprocessing

We use **Pandas** to load the dataset.

* **Action:** Read `predict.csv` into a dataframe.
* **Reshaping:** The input `x` (size) is reshaped into a 2D array (`[[...]]`) because Scikit-Learn expects a matrix format for features.

### Step 2: Polynomial Transformation (The Key Step)

Standard Linear Regression cannot fit a curve. To fix this, we use `PolynomialFeatures` from Scikit-Learn.

* **Logic:** We convert the input  into a polynomial set .
* **Code Concept:**
```python
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

```


* *Before:* `[size]`
* *After:* `[size, size^2]` (This allows the linear model to learn the curve).



### Step 3: Training the Model

We fit a standard **Linear Regression** model, but instead of training it on the original simple data, we train it on the **transformed polynomial data** (`x_poly`).

* **Math:** The model learns coefficients for both  and  ().

### Step 4: Making a Prediction

When the user enters a new size (e.g., `2500`), we cannot just pass `2500` to the model.

1. **Transform:** We first convert `2500` into `[2500, 2500^2]`.
2. **Predict:** The model calculates the price using these squared values.

### Step 5: Visualization

Finally, we use **Matplotlib** to compare the reality vs. the prediction.

* **Scatter Plot (Blue/Black):** Shows the actual data points from `predict.csv`.
* **Curve Line (Red):** Shows the polynomial regression line fitted by the model.
