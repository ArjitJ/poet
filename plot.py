import sys
import matplotlib.pyplot as plt
import numpy as np

avg = 1000
x = []
for line in open(sys.argv[1], 'r'):
    x.append(float(line.strip()))
x = np.convolve(x, np.ones(avg)/avg, mode='valid')
plt.plot(x)
plt.xlabel("Episode #n over any and all (agent, env) pairs")
plt.ylabel(f"Average reward in episodes [n, n + {avg - 1}]")
plt.show()
