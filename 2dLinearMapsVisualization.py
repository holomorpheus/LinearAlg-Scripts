# Created by: Gabriel Martins
# Modified from an earlier script by: Raibatak Das
# Date: Sep 14 2020

# Importing Libraries.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Naming trig functions and pi.
cos, sin, pi = np.cos, np.sin, np.pi;

#------------------------------------
# Defining the linear map

# Scaling Matrix.
a, b = 4/5, 2;
B = np.matrix([[a, 0], [0, b]]);

# Rotation Matrix.
theta = pi/6;
C = np.matrix([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]);

A = C*B
#------------------------------------
# Defining 4clovers

# How many clovers?
N = 6;

# How many leaves in a clover? If L = 0 you will get a circle.
L = 3;

# List of radii.
rad = np.array([i for i in range(1,N+1)]);

# Colors for the cloves.
colormap = cm.get_cmap('spring', len(rad));
colors = colormap(np.linspace(1,0,len(rad)));

# Define array of angles
anglegridsize = 100;
thetaspan = np.linspace(0, 2*pi, anglegridsize);

# Define the unit clover
rtheta = cos((L/2)*thetaspan)**2;
xclover = rtheta*cos(thetaspan);
yclover = rtheta*sin(thetaspan);
unit_clover = np.matrix([xclover,yclover]);

# Define different circles in the domain.
xyclovers = np.zeros((len(rad),2,anglegridsize));
for i in range(len(rad)):
    xyclovers[i,:,:] = rad[i]*unit_clover;

# Define image of circles in target space.
uvclovers = np.zeros((len(rad),2,anglegridsize));
for i in range(len(rad)):
    uvclovers[i,:,:] = A*xyclovers[i,:,:];

#------------------------------------
# Plotting

# Scope
scope  = rad[-1]+.5;

# Plot domain.
plt.figure(figsize=(5, 5), facecolor="w")
# Plot axes
plt.axhline(y=0, color='k', alpha=0.5)
plt.axvline(x=0, color='k',alpha=0.5)
# Plot cloves
for i in range(len(rad)):
    plt.plot(xyclovers[i,0,:], xyclovers[i,1,:], color=colors[i], alpha=0.8)
plt.grid(True)
plt.axis("equal")
plt.xlim([-scope, scope])
plt.ylim([-scope, scope])
plt.title("Original grid in x-y space")


# Plot target space.
plt.figure(figsize=(5, 5), facecolor="w")
# Plot axes
plt.axhline(y=0, color='k', alpha=0.5)
plt.axvline(x=0, color='k', alpha=0.5)
# Plot cloves
for i in range(len(rad)):
    plt.plot(uvclovers[i,0,:], uvclovers[i,1,:], color=colors[i], alpha=0.8)

plt.grid(True)
plt.axis("equal")
plt.xlim([-scope, scope])
plt.ylim([-scope, scope])
plt.title("Transformed grid in u-v space")

#------------------------------------

