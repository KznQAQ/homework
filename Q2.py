# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:02:43 2024

@author: daniel 駱
"""

import matplotlib.pyplot as plt

'''
Q3
'''    

n_max=40 
"F(50)跑超久 所以我設40"

def f_top_down(n):
    if n == 4 or n == 5:
        return 1
    elif n <= 3:
        return 0
    
    else:
        return f_top_down(n-1) + f_top_down(n-2)

def f_top_down_list(n):
    
    f_top_down_list_ = []
    for i in range(5, n+1):
        f_top_down_list_.append(f_top_down(i))
        
    return f_top_down_list_


r = list(range(5, n_max+1))

plt.figure(dpi = 300)
plt.plot(r, f_top_down_list(n_max), 'r')  
plt.title('Fibonacci Number F(n), top_down', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Nunber of F(4)', fontsize = 15)
plt.show()