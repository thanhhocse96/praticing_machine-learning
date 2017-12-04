#Machine Learning co ban - Linear Regression - Hoi quy tuyen tinh
#VD: Gia su can nang phu thuoc vao chieu cao
#Ta co bang can nang va chieu cao cua 1 nguoi
#Chieu cao:  147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183
#Can nang:   49,  50,  51,  54,  58,  59,  60,  62,  63,  64,  66,  67,  68
#Lap mo hinh hoi quy tuyen tinh

from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

# height (cm)
X = np.array(
    [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

#------Giai bai toan toi uu---------
#pinv(a): Pseudo Inverse - gia nghich dao cua X
#Nghiem toi uu: w = pinv(A) . b = pinv(X^T . X) . X^T . y

#(1) Building Xbar
#Xbar: 
#Tao vector don vi one kich thuoc (15,1): 15 hang x 1 cot
#X.shape: Tra ve array chua kich thuoc cac chieu cua matrix X:
#X.shape = (15, 1) => X.shape[0] = 15
#numpy.one([shape]): tao ma tran don vi voi kich thuoc shape
one = np.ones((X.shape[0], 1))
#numpy.concatenate((sequence of array_like(same shape)), axis)
Xbar = np.concatenate((one, X), axis=1)

#(2) Calculating weights of the fitting line
#numpy.dot(a, b, out=None): Tich 2 ma tran (2-D arrays)
#                      hoac Tich vo huong 2 vector (1-D arrays)
#A = Xbar^T . Xbar
A = np.dot(Xbar.T, Xbar)
#b = Xbar^t . y
b = np.dot(Xbar.T, y)
#-> w = pinv(A) . b
w = np.dot(np.linalg.pinv(A), b)
# print(w)


#(3) Fitting line: y = w_1 . x + w_0
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(145, 185, 2)
y0 = w_0 + w_1 * x0

#(4) Drawing the fitting line
plt.plot(X, y, 'bo')   #data
plt.plot(x0, y0)       #fitting line
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()