"""
Created on Fri Jan 22 14:19:09 2021

Original author: Daidalos
Modified by: Gabriel Martins
"""

import matplotlib.pyplot as plt
import vectorplot as vp

# Define points and vectors
A = [1,1]
B = [3,5]
labels_AB = ["A", "B", r"$\vec{v}$"]

C = [-1,6]
D = [-3,-2]
labels_CD = ["C", "D", r"$\vec{u}$"]

# Define the tile for the plot
title = "Gabriel's vector plot"

# Create a vector with all of the x coordinates
# and another with all of the y coordinates of
# the points in the plot
x_coordinates = [A[0],B[0],C[0],D[0]]
y_coordinates = [A[1],B[1],C[1],D[1]]

# Define figure and axes objects.
fig, ax = plt.subplots()

# Plot vectors
vp.plotvector(A,B,labels_AB,ax)
vp.plotvector(C,D,labels_CD,ax)

#----------------------------------------------------
# Plot adjustments

# Define the limits of the plot
x1, x2 = min(x_coordinates)-1, max(x_coordinates)+1;
y1, y2 = min(y_coordinates)-1, max(y_coordinates)+1;

ax.set_xlim(x1,x2)
ax.set_ylim(y1,y2)

# Show the coordinate grid
ax.grid(True)

# Plot axes.
ax.axhline(y=0, color='k', alpha=0.5)
ax.axvline(x=0, color='k', alpha=0.5)

# Set a title for the plot
ax.set_title(title,fontsize=14)

#----------------------------------------------------
# Show plot or save?
plt.show()
#plt.savefig('vectorplot.png', bbox_inches='tight')
#plt.close()
