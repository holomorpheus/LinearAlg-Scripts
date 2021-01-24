"""
Created on Fri Jan 22 14:19:09 2021

Author: Daidalos
Modified: Gabriel Martins
"""

from numpy import sqrt

def plotvector(A,B,labels,ax):
    ''' Plots arrow connecting point A to point B
        labels = [source, target, vector]
        ax = axis object from matplotlib. '''
    
    # Coordinates of the corresponding vector
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    
    vec_magnitude = sqrt(dx**2+dy**2)
    
    # Coordinates of the normal vector
    nx, ny = -dy/vec_magnitude, dx/vec_magnitude
    
    # Lengths of line and head of arrow
    head_length = 0.3
    line_length = vec_magnitude - head_length
    
    # Rescaled coordinates for the line portion of the arrow
    dxl = dx * (line_length / vec_magnitude)
    dyl = dy * (line_length / vec_magnitude)
    
    # Plotting
    ax.scatter(A[0],A[1],color='black')
    ax.scatter(B[0],B[1],color='black')
    
    ax.arrow(A[0], A[1], dxl, dyl, head_width=0.6*head_length, head_length=head_length, fc='lightblue', ec='black')
    
    ax.annotate(labels[0], (A[0]-.6*nx,A[1]-.6*ny),fontsize=14)
    ax.annotate(labels[1], (B[0]-.6*nx,B[1]-.6*ny),fontsize=14)
    ax.annotate(labels[2], (A[0]+dx/2+.5*nx,A[1]+dy/2+.5*ny),fontsize=14)
    

