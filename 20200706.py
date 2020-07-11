import numpy as np
A = np.array([1, 2, 3, 4]).reshape(2, 2)
print(A)

B = np.array([100, 200])
print(B)

C = A + B
print(C)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)
print(C)

F = np.array([8.66, 5.0])
S = np.array([20, 0])
W = np.dot(F, S)
print(W)


f = np.linalg.norm(F)
s = np.linalg.norm(S)
rad = np.radians(30)
w = f*s*np.cos(rad)
print(w)


a = np.array([1, 2, 0])
b = np.array([0, 1, -1])
c = np.cross(a, b)
print(c)

import math
import numpy as np

data = [0.0, 0.28, 0.57, 0.85, 1.14, 1.42, 1.71, 1.99, 2.28, 2.57, 2.85, 3.14]
##math.sin(data)

print(np.sin(data))
