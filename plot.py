import sys
import matplotlib.pyplot as plt
import numpy as np

avg = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
x = []
y = []
iter = 0
for line in open(sys.argv[1], 'r'):
    line = line.strip().split()
    if "Iter" in line[0]:
        iter = int(line[1])
    else:
        x.append(float(line[1]))
        y.append(iter)
x = np.convolve(x, np.ones(avg)/avg, mode='valid')
# avg = 100
y = np.convolve(y, np.ones(avg)/avg, mode='valid')
plt.plot(x)
y = [10000 * (y[i] - y[i-1]) for i in range(1, len(y))]
# avg = 10
y = np.convolve(y, np.ones(avg)/avg, mode='valid')
plt.plot(y)
plt.legend([f"Average reward in episodes [n, n + {avg - 1}]", "Scaled and smoothened gradient of number of iterations completed"])
plt.xlabel("Episode #n over any and all (agent, env) pairs")
plt.show()
