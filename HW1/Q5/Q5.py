#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time
from tqdm import tnrange, tqdm_notebook
import matplotlib.pyplot as plt


# In[2]:


class Fast3Sum:
    def __init__(self, input_data):
        self.data = input_data
        self.data.sort()
        
    def twosum(self, target):
        counter = 0
        min = 0
        max = len(self.data) - 1
        
        while min < max:
            if self.data[min] + self.data[max] == target:
                counter += 1
                min += 1
            elif self.data[min] + self.data[max] < target:
                min += 1
            else:
                max -= 1
        return counter
    
    def threesum(self):
        counter = 0
        for i in tnrange(len(self.data)):
            counter += self.twosum(-self.data[i])
        return counter
    
            
    def runtime(self):
        time_start = time.time()
        self.threesum()
        time_finish = time.time()
        time_run = time_finish - time_start
        return time_run


# In[3]:


input_data_8 = np.loadtxt('Q5_dataset/8int.txt', int)
input_data_32 = np.loadtxt('Q5_dataset/32int.txt', int)
input_data_128 = np.loadtxt('Q5_dataset/128int.txt', int)
input_data_512 = np.loadtxt('Q5_dataset/512int.txt', int)
input_data_1024 = np.loadtxt('Q5_dataset/1024int.txt', int)
input_data_4096 = np.loadtxt('Q5_dataset/4096int.txt', int)
input_data_4192 = np.loadtxt('Q5_dataset/4192int.txt', int)
input_data_8192 = np.loadtxt('Q5_dataset/8192int.txt', int)

bit_8 = Fast3Sum(input_data_8)
bit_32 = Fast3Sum(input_data_32)
bit_128 = Fast3Sum(input_data_128)
bit_512 = Fast3Sum(input_data_512)
bit_1024 = Fast3Sum(input_data_1024)
bit_4096 = Fast3Sum(input_data_4096)
bit_4192 = Fast3Sum(input_data_4192)
bit_8192 = Fast3Sum(input_data_8192)


# In[4]:


input_number = [8, 32, 128, 512, 1024, 4096, 4192, 8192]
runtime = [bit_8.runtime(), bit_32.runtime(), bit_128.runtime(), bit_512.runtime(),           bit_1024.runtime(), bit_4096.runtime(), bit_4192.runtime(), bit_8192.runtime()]


# In[5]:


plt.figure
plt.plot(input_number, runtime, 'r' )
plt.title('time cost as a function of input numbers')
plt.xlabel('input number')
plt.ylabel('time cost (s)')
plt.savefig('./plot.jpg')
plt.show()


# In[ ]:




