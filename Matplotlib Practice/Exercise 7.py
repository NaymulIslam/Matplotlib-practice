import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x= [0,1/3,2/3,1]
y= [0,1/3,2/3,1]

x1=[0,1/3,2/3,1]
y1=[0,1/3,2/3,1]

plt.figure(figsize=(7,5),dpi=100)

plt.plot (x1,y1,'b',label='45 Degree Line')
plt.plot(x,y,'r.--', label='Lorenz Curve') 

#nadim


plt.title ("Gini Coefficient", fontdict={'fontname':'Times New Roman', 'fontsize': 20})

# X and Y labels
plt.xlabel("Cumulative Relative Freqency of Income", fontdict={'fontname': 'Arial', 'fontsize': 15})
plt.ylabel("Cumulative Relative Freqency of Population",fontdict={'fontname': 'Arial', 'fontsize': 15})

plt.xticks([0,1/3,2/3,1])
plt.yticks([0,1/3,2/3,1])




plt.legend()



plt.show()