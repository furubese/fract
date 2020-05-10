import matplotlib.pyplot as plt
import matplotlib.patches as pat
import math

x = []
y = []
for i in range(3):
    x.append(i)
    y.append(i*i)

plt.plot(x,y)
plt.show()