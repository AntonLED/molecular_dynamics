from dependences import U
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(10, 10))
plt.grid()


x = np.linspace(start=1.5, stop=10, num=10000)
y = U(np.linspace(start=1.5, stop=10, num=10000))

plt.vlines(2, -100, 100, linestyles=':', colors='blue')
plt.vlines(2 * 2**(1/6), -100, 100, linestyles=':', colors='red')
plt.hlines(-10, -1, 10, linestyles=':', colors='orange')

plt.xlim(-1, 10)
plt.ylim(-100, 100)

plt.plot(x, y)
plt.ylabel("energy")

plt.show()

