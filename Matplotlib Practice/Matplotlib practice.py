
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x= [0,1,2,3,4]
y= [0,2,4,6,8]

# Resize the graph (dpi specifies pixels per inch, when saving prbly sould be 300 if possible)

# If dpi is too high graph will be really big. around 100 is okay
plt.figure(figsize=(5,3),dpi=200)

# Line 1

# keyword Argument Notation
# plt.plot(x,y, label='2x', color='Blue', linewidth= 2, marker='.',linestyle='--',markersize=10, markeredgecolor='red')

#shorthand notation
# fmt= '[color][marker][line]'
plt.plot(x,y,'b^--', label='2x') 

#  Line 2
# Select interval we want to plot points at
x2= np.arange(0,4.5,0.5)

# plt.plot(x2,x2**2, 'r.-', label='X^2')

#Plot part of the Graph as line
plt.plot(x2[:5],x2[:5]**2, 'r', label='X^2')

# Plot remainder of graph as a dot
plt.plot(x2[4:],x2[4:]**2, 'r.--')

# Add a title (specify font parameters with fontdict)
plt.title ("Our First Graph", fontdict={'fontname':'Times New Roman', 'fontsize': 20})

# X and Y labels
plt.xlabel("X Axis", fontdict={'fontname': 'Arial', 'fontsize': 15})
plt.ylabel("Y Axis",fontdict={'fontname': 'Arial', 'fontsize': 15})

# X and Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10,12,14,16,18])

# Add a Legend
plt.legend()

# Save figure (dpi 300 is good when saving, so graph has high resolution)
# plt.savefig('mygraph.png', dpi=300)

# show plot
plt.show()

### Bar charts

labels= ['A', 'B', 'C']
values= [1,4,2]

plt.figure(figsize=(6,4))

bars = plt.bar(labels, values)

patterns=['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')

plt.xlabel('Country',fontdict={'fontname':'Times New Roman','fontsize':20})
plt.ylabel('Birth Rate',fontdict={'fontname':'Arial', 'fontsize':20})


plt.show()