import matplotlib.pyplot as plt
import random
import numpy as np
from primePy import primes

cos = np.cos(np.pi/8)
sin = np.sin(np.pi/8)

f1 = np.array([[cos, -sin], [sin, cos]])
prime_list = primes.first(16000)
p1 = prime_list[:3999]
p2 = prime_list[4000: 7999]
p3 = prime_list[8000: 11999]
p4 = prime_list[12000:]

x = [0]
y = [0]

for i in range(799999):
    p = random.randint(1, 100)
    if 1 <= p <= 30:
        prime = random.choice(p1)
    if 31 <= p <= 60:
        prime = random.choice(p2)
    if 61 <= p <= 90:
        prime = random.choice(p3)
    else:
        prime = random.choice(p4)

    f2 = np.array([[1, 11/prime, 11/prime],
                   [0, 1, 11/prime]])
    new_dot = np.array([x[-1], y[-1], 1]).transpose()
    new_dot = f2 @ new_dot
    new_dot = f1 @ new_dot

    x.append(new_dot[0])
    y.append(new_dot[1])

plt.figure(figsize=(10, 10), dpi=300)
plt.scatter(x, y, s=0.00095, c='blueviolet')
plt.axis("on")
plt.show()