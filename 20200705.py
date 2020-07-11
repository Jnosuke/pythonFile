import numpy as np
import math

A = np.array([10, 20, 30, 40]).reshape(2, 2)
print(A)

B = A + 5
print(B)

print("+", A - 5)
print("*", A * 5)
print("/", A / 5)


p0 = np.array((1, 1))
p1 = np.array((6, 4))
A = p1 - p0

print(A)


a_norm = np.linalg.norm(A)
print(a_norm)
X = 5**2 + 3**2
x = math.sqrt(X)
print(x)

A = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
print(A)

print(A.sum())
print(A.sum(0))
print(A.sum(1))


A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([10, 20, 30, 40]).reshape(2, 2)

C = A + B
print(C)
D = A * B
print(D)
E = A / B
print(E)
