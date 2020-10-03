"""
Introduction to SymPy and Row Reduction

Created on Sep 27 2020
Last Modified on Oct 1 2020

@author: gabrielmartins
"""

# Import the SymPy library
import sympy as sm

# # Import the matrixGenerator module
# import matrixGenerator as mg

# Shorthand for writing fractions
rt = sm.Rational;

# Warning:
""" While rt(1,2) is the same as rt(1/2)
    rt(1,3) is pretty different than rt(1/3)
    be careful. """

# Defining vectors
u = sm.Matrix( [ rt(1,2), -2, 3 ] );
print("The vector u is:")
sm.pprint(u)
print("The vector v is:")
v = sm.Matrix( [ -2, 1, rt(1,3)] );
sm.pprint(v)

# Defining a matrix using the vector u and v as rows
A = sm.Matrix([u.T, v.T]);
print("The generating matrix for u and v is:")
sm.pprint(A)

# Defining a matrix
M = sm.Matrix([ [2, 1, 0], [1, rt(1,2), 0], [0, -1, 1] ]);
print("The matrix M is:")
sm.pprint(M)

# Row reduce matrix
RM, pivots = M.rref()
print("The reduced row echelon form of M is:")
sm.pprint(RM);

# # Generate a random matrix
# """ First argument: rows
#     Second argument: columns
#     Third argument: rank
#     Fourth and fith arguments: Control how complicated the matrix will be """
# A = mg.generate(4,5,3,1,3);

""" Some other cool stuff SymPy can do """

# Define variable x
x = sm.symbols('x')
print("Here's a polynomial. If you use the console, you can print in LaTeX.")
sm.pprint(x**2+3)

# Shorthand for the exponential and square root functions, and constant π
exp = sm.exp;
pi = sm.pi;

# Print Euler's identity
i = sm.symbols('i');
theta = sm.symbols('theta');
print("Here's Euler's Identity")
sm.pprint(sm.Eq(exp(i*theta),-1))

# Integrate a function
# sm.pprint(sm.integrate(x**3, x))


