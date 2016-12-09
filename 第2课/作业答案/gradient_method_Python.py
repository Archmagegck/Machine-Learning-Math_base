# -*- coding: utf-8 -*-
"""

@author: sss
"""
import numpy as np

def gradient(A,b,x0,epsilon):
    iteration = 0
    x = x0;
    grad = 2*(A.dot(x)+b)
    while(np.linalg.norm(grad)>epsilon):
        iteration = iteration+1
        t = np.linalg.norm(grad)**2/(2*grad.T.dot(A).dot(grad))
        x = x - t*grad
        grad = 2*(A.dot(x)+b)
        fun_val = x.T.dot(A).dot(x)+2*b.T.dot(x)
        print 'iter_number = {0} fun_val = {1}'.format(iteration,fun_val)
        
A = np.array([[1.0,0],[0,2.0]])
b = np.array([[0.0],[0]])
x0 = np.array([[2.0],[1.0]])
epsilon = 1e-5
gradient(A,b,x0,epsilon)
        
    