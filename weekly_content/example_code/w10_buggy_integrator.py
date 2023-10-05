from math import *
import matplotlib.pyplot as plt

# Define the parameters in the problem
a = 1
b = 3

N = 10
dx = (b - a) / N

alpha = 10
mu = 1.5


# Define the mathematical function to integrate over
def f(x):

    # make mu and alpha global variables so they can
    # be used anywhere
    global mu, alpha
    alpha = 10
    mu = 1.0

    # return the value of the function
    return alpha * exp(-mu * x)

# Define the exact value of the integral for comparison
A_exact = alpha / mu * (exp(-mu * a) - exp(-mu * b))


# Define a Python function to approximate the integral using
# the trapezium rule
def integrate(N):

    # initialise the area under the curve
    A = 1/2 * (f(a) + f(b)) * dx

    # compute the sum in the integration formula
    for i in range(1, N):
        x_i = a + i * dx
        A += f(x_i) * dx
        
    # return the result
    return A


# Now we use a loop to compute the integrals for different
# values of N (number of trapezoids)

N_list = [2**n for n in range(2, 7)]
A_list = []

for n, N in enumerate(N_list):
    A_list.append(integrate(N))
    print('The area when N =', N, 'is:', A_list[n])

print('The exact area is', A_exact)
