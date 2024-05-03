# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:17:50 2024

@author: daniel 駱
"""

import matplotlib.pyplot as plt
import time
import numpy as np

#設定F(n)的n
n = int(input('輸入F(n)之n：'))
start_time = time.time()
execution_time=np.zeros(n+1)
def f_top_down(n):
    if n == 0 or n == 1:
        return n
    else:
        return f_top_down(n-1) + f_top_down(n-2)
    
def f_top_down_list(n):
    
    f_top_down_list_ = []
    for i in range(2, n+1):
        f_top_down_list_.append(f_top_down(i))
        execution_time[i] = time.time() - start_time
    return f_top_down_list_


a = f_top_down_list(n)

r = list(range(5, n+1))


plt.figure(dpi = 300)
plt.plot(f_top_down_list(n), a, 'r')   # red line without marker
plt.title('Fibonacci Number F(n), top_down', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('F(n)', fontsize = 15)

plt.figure(dpi = 300)
plt.plot( execution_time, 'r')   # red line without marker
plt.title('T(n), top_down', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('F(n)', fontsize = 15)
plt.show()