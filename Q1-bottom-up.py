# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:37:24 2024

@author: daniel 駱
"""
import matplotlib.pyplot as plt
import time
import numpy as np
#Fibonacci Number F(n) = F(n-1) + F(n-2)

'Q1'

"bottom-up" 
n=10000000   
start = time.time()  
fib_bottom_up=np.zeros(n+1)      
fib_bottom_up[1]=1
timeup1=np.zeros(n+1)

for i in range(2, n+1):
    fib_bottom_up[i] = fib_bottom_up[i-1]+fib_bottom_up[i-2]
    timeup1[i] =float(  time.time() )-start  
'n只到好像100，太快跑完的所以時間都是0，所以我數字調大一點，此時才能看出T(n)=O(n)'

plt.figure(dpi = 300)
plt.plot(fib_bottom_up, 'r')   # red line without marker
plt.title('Fibonacci Number F(n) = F(n-1) + F(n-2), bottom_up', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('F(n)', fontsize = 15)

plt.figure(dpi = 300)
plt.plot(timeup1, 'r')   # red line without marker
plt.title('Execution time of  F(n) , bottom_up', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Execution timee F(n)', fontsize = 15)

plt.show()

