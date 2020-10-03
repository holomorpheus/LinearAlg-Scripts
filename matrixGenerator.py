"""
Matrix Generator

Created on Oct 1 2020

by Gabriel Martins
"""

import random as rd
import sympy as sm

def random_nonzero(m,n):
    s = 0;
    while s == 0:
        s = rd.randrange(m,n);
    return s

def scale(A,m,s):
    ''' m = row to be scaled
        s = scalar '''
    
    B = A[:,:];
    
    if s == 0:
        return B
    
    B[m,:] = s*B[m,:];
    
    return B

def switch(A,i,j):
    ''' i and j are the indices of rows to be switched. '''
    
    B = A[:,:];    
    B[i,:], B[j,:] = B[j,:], B[i,:];
    
    return B

def shear(A,i,j,s):
    ''' Adds s*j-th row to the i-th row. '''
    
    B = A[:,:]; 
    B[i,:] = B[i,:] + s*B[j,:];
    
    return B

def echelon(m, n, rank, scope):
    ''' m: number of rows
        n: number of columns
        rank: desired rank of the matrix
        scope: limits the possible numbers in the matrix'''
        
    # Define matrix of zeros
    A = sm.Matrix([[0]*n]*m);
    
    if rank == 0:
        return A;
    else:       
        # Define where the pivots will be
        # Always have a pivot at 1st column
        pivs = rd.sample(range(1,n),rank-1);
        pivs.sort()
        pivots = [0]+pivs
        
        # Define pivots
        for i in range(rank):
            A[i,pivots[i]] = 1;
            for j in range(pivots[i]+1,n):
                A[i,j] = rd.randrange(-scope,scope+1);
        
        return A, rank
    
def complicate(A, rank, hardness, scope):
    ''' A: mxn matrix
        rank: rank of A
        hardness: number of row reduction operations performed
        scope: limit on the scalars used in operations. '''
        
    B = A[:,:];
    m = A.shape[0];
    ops = [scale, switch, shear]
    
    for i in range(1,m):
        s = random_nonzero(-scope,scope+1);
        B = ops[2](B,i,0,s);
        row = rd.randrange(i);
        s = random_nonzero(-scope,scope+1);
        B = ops[2](B,i,row,s);

    for i in range(hardness):
        j = rd.randrange(3);
        
        if j == 0:
            row = rd.randrange(m);
            s = random_nonzero(-scope,scope+1);
            B = ops[j](B,row,s);
            
        if j == 1:
            rows = rd.sample(range(m),2);
            B = ops[j](B,rows[0],rows[1]);
        
        if j ==2 :
            rows = rd.sample(range(m),2);
            s = random_nonzero(-scope,scope+1);
            B = ops[j](B,rows[0],rows[1],s);
    
    return B;

def generate(m, n, rank, scope, hardness):
    ''' m: number of rows
        n: number of columns
        rank: desired rank of the matrix
        scope: limits the possible numbers in the matrix
        hardness: number of row reduction operations performed '''
    
    A, rk = echelon(m, n, rank, scope);
    
    A = complicate(A, rank, hardness, scope);
    
    return A

# # Generate a matrix and print
# A = generate(5,10,4,2,4)
# print("Here is a random 5x10 matrix of rank 4:")
# sm.pprint(A)

# print("Here is its reduced row echelon form:")
# sm.pprint(A.rref()[0])

