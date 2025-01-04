import matplotlib.pyplot as plt
from random import randint
import numpy as np

f1 = np.array([[0.14, 0.01, -0.08], [0, 0.51, -1.31]])
f2 = np.array([[0.43, 0.52, 1.49], [-0.45, 0.5, -0.75]])
f3 = np.array([[0.45, -0.49, -1.62], [0.47, 0.47, -0.74]])
f4 = np.array([[0.49, 0, 0.02], [0, 0.51, 1.62]])

x = [0]
y = [0]

for i in range(0, 999999):
    new_dot = np.array([x[i], y[i], 1])
    p = randint(1, 100)

    if 1 <= p <= 1:
        new_dot = f1 @ new_dot.transpose()

    elif 2 <= p <= 33:
        new_dot = f2 @ new_dot.transpose()

    elif 34 <= p <= 65:
        new_dot = f3 @ new_dot.transpose()

    else:
        new_dot = f4 @ new_dot.transpose()

    x.append(new_dot[0])
    y.append(new_dot[1])

plt.scatter(x, y, s=0.00095, c='red')
plt.axis("on")
plt.show()