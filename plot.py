import sys
import matplotlib.pyplot as plt
import numpy as np


x = []
for line in open(sys.argv[1], 'r'):
    x.append(float(line.strip()))
x = np.convolve(x, np.ones(1000)/1000, mode='valid')
plt.plot(x)
plt.show()
