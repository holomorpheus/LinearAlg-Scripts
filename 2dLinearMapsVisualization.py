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
#a, b = 4/5, 2;
#S = np.matrix([[a, 0], [0, b]]);

# Rotation Matrix.
#theta = pi/6;
#R = np.matrix([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]);

# Shear Matrix.
A = np.matrix([[1, 1], [0, 1]]);


#------------------------------------
# Aesthetic choices

# How many flowers?
N = 6;

# How many petals in a flower? If L = 0 you will get a circle.
L = 8;

# How many gridpoints?
anglegridsize = 256;

# Which colormap?
colormapname = 'viridis'

# Plot horizontal or vertical bounds?
hbounds = False;
vbounds = False;


#------------------------------------
# Defining flowers

# List of radii.
rad = np.array([i for i in range(1,N+1)]);

# Colors for the flowers.
colormap = cm.get_cmap(colormapname, len(rad));
colors = colormap(np.linspace(.8,.2,len(rad)));

# Define array of angles
thetaspan = np.linspace(0, 2*pi, anglegridsize);

# Define the unit flower
rtheta = np.abs(cos((L/2)*thetaspan))**.6;
xflower = rtheta*cos(thetaspan);
yflower = rtheta*sin(thetaspan);
unit_flower = np.matrix([xflower,yflower]);

# Define different circles in the domain.
xyflowers = np.zeros((len(rad),2,anglegridsize));
for i in range(len(rad)):
    xyflowers[i,:,:] = rad[i]*unit_flower;

# Define image of circles in target space.
uvflowers = np.zeros((len(rad),2,anglegridsize));
for i in range(len(rad)):
    uvflowers[i,:,:] = A*xyflowers[i,:,:];

#------------------------------------
# Plotting

# Scope
scope  = rad[-1]+.5;

# Define figure and axes objects.
fig, ax = plt.subplots(1,2,figsize=(10, 5))

# Domain

# Plot axes
ax[0].axhline(y=0, color='k', alpha=0.5)
ax[0].axvline(x=0, color='k',alpha=0.5)

# Plot horizontal bounds.
if hbounds:
    ax[0].axhline(y=rad[-1], color='k',alpha=0.5)
    ax[0].axhline(y=-rad[-1], color='k',alpha=0.5)

# Plot vertical bounds.
if vbounds:
    ax[0].axvline(x=rad[-1], color='k',alpha=0.5)
    ax[0].axvline(x=-rad[-1], color='k',alpha=0.5)

# Plot flowers in the domain.
for i in range(len(rad)):
    ax[0].plot(xyflowers[i,0,:], xyflowers[i,1,:], color=colors[i], alpha=0.8)
ax[0].grid(True)
ax[0].axis("equal")
ax[0].set_xlim([-scope, scope])
ax[0].set_ylim([-scope, scope])
ax[0].set_title("Original grid in x-y space")

# Target Space

# Plot axes.
ax[1].axhline(y=0, color='k', alpha=0.5)
ax[1].axvline(x=0, color='k', alpha=0.5)

# Plot horizontal bounds.
if hbounds:
    ax[1].axhline(y=rad[-1], color='k',alpha=0.5)
    ax[1].axhline(y=-rad[-1], color='k',alpha=0.5)

# Plot vertical bounds.
if vbounds:
    ax[0].axvline(x=rad[-1], color='k',alpha=0.5)
    ax[0].axvline(x=-rad[-1], color='k',alpha=0.5)

# Plot flowers in target space.
for i in range(len(rad)):
    ax[1].plot(uvflowers[i,0,:], uvflowers[i,1,:], color=colors[i], alpha=0.8)

ax[1].grid(True)
ax[1].axis("equal")
ax[1].set_xlim([-scope, scope])
ax[1].set_ylim([-scope, scope])
ax[1].set_title("Transformed grid in u-v space")
