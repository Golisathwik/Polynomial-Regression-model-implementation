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

We arrange these sums into the matrix equation X A = B to solve for the unknown coefficients A.

$$
\begin{bmatrix}
n & \Sigma x & \Sigma x^2 \\\\
\Sigma x & \Sigma x^2 & \Sigma x^3 \\\\
\Sigma x^2 & \Sigma x^3 & \Sigma x^4
\end{bmatrix}
\cdot
\begin{bmatrix}
a_0 \\\\
a_1 \\\\
a_2
\end{bmatrix}
=
\begin{bmatrix}
\Sigma y \\\\
\Sigma xy \\\\
\Sigma x^2y
\end{bmatrix}
$$

Substituting the values from our table (n=4):

$$
\begin{bmatrix}
4 & 10 & 30 \\\\
10 & 30 & 100 \\\\
30 & 100 & 354
\end{bmatrix}
\cdot
\begin{bmatrix}
a_0 \\\\
a_1 \\\\
a_2
\end{bmatrix}
=
\begin{bmatrix}
29 \\\\
96 \\\\
338
\end{bmatrix}
$$

### Step 3: Final Model Solution
By solving the matrix equation (calculating $X^{-1} \cdot B$), we get the optimal values:

$$
\begin{bmatrix} a_0 \\ a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} -0.75 \\ 0.95 \\ 0.75 \end{bmatrix}
$$

**The Final Best-Fit Equation:**
$$y = -0.75 + 0.95x + 0.75x^2$$
