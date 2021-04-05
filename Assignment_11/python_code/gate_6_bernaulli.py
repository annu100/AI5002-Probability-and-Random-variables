import numpy as np
from scipy.stats import binom
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
P_H=0.3
P_T=0.7


#X and Y are binomial random variables
simlen = int(1e4)
#plot the bar grapgh for PMF
x=[0,1]
p=0.3 #robability for head
plt.figure(1)
plt.bar(x,bernoulli.pmf(x,p),width=0.1,color=["r","b"])
plt.title("Probability mass function for biased coin getting head")
plt.xlabel("data points")
plt.ylabel("Probability")
plt.show()
plt.figure(2)
plt.bar(x,bernoulli.cdf(x,p),width=0.1,color=["r","b"])
plt.title("Cummulative density function for biased coin getting head")
plt.xlabel("data points")
plt.ylabel("Probability")
plt.show()
#Probability for getting first head in 5th toss =0.07203 calculated from theory)
X = binom.rvs(n=5, p=0.07203, size=simlen)
X_count = np.zeros(5)
for i in range(5):
    X_count[i] = np.count_nonzero(X == i)
plt.figure(3)
plt.stem(X, linefmt='C2--', markerfmt='C2o', label='X=first Head in 5th toss')
plt.xlabel('Simulation ')
plt.ylabel('X=first Head in 5th toss')
plt.title('Plot showing X=first Head in 5th toss')
plt.legend()
plt.show()
