# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 10:21:37 2016

@author: gck
"""
import pandas as pd
from numpy import *

#计算损失函数
def computeCost(X, y, theta):
    return sum( (X * theta - y) ** 2) / (2 * m);
    
#梯度下降法，求目标函数最小值
    #X 第一列为1的样本数据
    #num_iters 迭代次数
    #epsilon 最小差值
def gridentDesent(X, y, theta, alpha, num_iters， epsilon = 0.0001):
    m = shape(X)[0];
    J_history = zeros((m,1));
    for iter in range(num_iters):
        theta = theta - alpha * 1/m (X.T * (X * theta -y));
        temp = 0;
        J_history[iter] = computeCost(X, y, theta);
        if (J_history[iter] - temp) < epsilon :
            break;
        temp = J_history[iter];  
    return theta, J_history;
        
def ex2():
    X = mat([[1,2,3],[1,5,6],[1,8,9]]);
    y = array([4,5,6]);
    theta = zeros((shape(X)[0],1));
    alpha = 0.01;
    num_iters= 50;
    (best_theta, J_history) = gridentDesent();
    print "最好的theta是%d，损失函数为%d" % (best_theta, J_history[-1]);
    
    