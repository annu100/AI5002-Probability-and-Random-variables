import numpy as np
# import uniform distribution
from scipy.stats import uniform
from matplotlib import pyplot as plt
import pandas as pd
#for latex equations
#from Ipython.display import Math,latex
print("$V=-2ln(1-U)$")
uniform_data=np.linspace(0,1,10000)
plot1=plt.figure(1)
fx=uniform.pdf(uniform_data,loc=0,scale=1)
plt.plot(uniform_data,fx)
plt.title("probability density function of $U$\n")
plt.xlabel("$u$")
plt.ylabel("$f_U(u)$")
plot2=plt.figure(2)
v=np.linspace(0,10,100)
plt.plot(v,1-np.exp(-v/2))
plt.title("Cummulative(CDF) of random variable $V$\n")
plt.xlabel("$v$")
plt.ylabel("$F_V(v)$")
plot2=plt.figure(3)
plt.plot(v,np.exp(-v/2)/2)
plt.title("Probability density function(PDF) of random variable $V$\n")
plt.xlabel("$v$")
plt.ylabel("$f_V(v)$")
plt.show()


