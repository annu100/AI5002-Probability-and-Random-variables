import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

#Given probability transition matrix
P=np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,1/3,1/3,1/3,0],[0,0,1/3,1/3,1/3],[0,0,0,0,1]])
P=np.reshape(P,(5,5))
A=P.T
#Stationary distribution is eigen vector of P transpose
eigvals,eigvecs=la.eig(A)
print("Eigen values are:")
print(eigvals)
print("Eigen vectors(stationary distribution) are :")
print(eigvecs)
