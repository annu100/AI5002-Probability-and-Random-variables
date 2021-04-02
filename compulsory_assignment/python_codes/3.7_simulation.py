import numpy as np
from scipy.stats import binom
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
P_A=0.5
P_B=0.5


#X and Y are binomial random variables
simlen = int(1e4)
#plot the bar grapgh for PMF
x=[0,1]
p=0.5
plt.figure(1)
plt.bar(x,bernoulli.pmf(x,p),width=0.1,color=["r","b"])
plt.title("Probability mass function")
plt.xlabel("data points")
plt.ylabel("Probability")
plt.show()
plt.figure(2)
plt.bar(x,bernoulli.cdf(x,p),width=0.1,color=["r","b"])
plt.title("Cummulative density function")
plt.xlabel("data points")
plt.ylabel("Probability")
plt.show()
X = binom.rvs(n=6, p=0.5, size=simlen)
X_count = np.zeros(6)
for i in range(6):
    X_count[i] = np.count_nonzero(X == i)
N = 6 * np.ones(simlen)
Y = N - X
Y_count = np.zeros(6)
for i in range(6):
    Y_count[i] = np.count_nonzero(Y == i)
Z = X - Y
Z_count = np.zeros(13)
y_range = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
for i in range(6):
    Z_count[i] = np.count_nonzero(Z == y_range[i])

plt.figure(3)
plt.stem(Z, linefmt='C2--', markerfmt='C2o', label='Z = # Heads - # Tails')
plt.xlabel('Simulation ')
plt.ylabel('Z=Heads - Tails in n=6 trials')
plt.title('Plot showing Heads number -  Tails number')
plt.legend()
plt.show()
