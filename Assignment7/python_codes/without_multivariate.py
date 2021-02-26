import numpy as np
from math import e
from math import pi
import math
import matplotlib.pyplot as plt

sample_size= 100000

mu1, sigma1= 1, 1
mu2, sigma2= 2, 2
combined_mu= mu1 + mu2
combined_var= sigma1*2 + sigma2*2
combined_sigma= math.sqrt(combined_var)

#Simulations using Gaussian R.V:
sample_X= np.random.normal(mu1, sigma1, sample_size)
sample_Y= np.random.normal(mu2, sigma2, sample_size)

#finding individual mean and variances:
mean_X = np.mean(sample_X)
var_X = np.var(sample_X)
mean_Y = np.mean(sample_Y)
var_Y = np.var(sample_Y)
mean_added = mean_X+mean_Y
var_added = var_X+var_Y
sd = np.sqrt(var_added)

#print(sample_X)
#print(sample_Y)

#adding individual gaussian r.v and forming new transformed r.v
U=[]
for i in range(0,sample_size):
    U.append(sample_X[i] + sample_Y[i])
    
U = np.array(U)
 
#finding mean and var of the transformed r.v 
mean_U= np.mean(U)
var_U = np.var(U)

#finding pdf:
f_U = (1.0/ math.sqrt(2*pi*var_U))*np.exp((-(U-mean_U)*2/(2*var_U)))

#printing all the mean and variances:
print("mean and var of sample_X are: ", mean_X,"and", var_X)
print("mean and var of sample_Y are: ", mean_Y,"and", var_Y)
print("sum of individual means and variances of simulated X and Y: ", mean_added ,"and", var_added )
print("sum of individual means and variances theoritically: ", combined_mu ,"and", combined_var )
print("mean and var of transformed R.V. U are: ", mean_U, var_U)

#simulating new gaussian with theoritical mean and variances:
sample_U= np.random.normal(combined_mu, combined_sigma , sample_size)

mean_sample_U = np.mean(sample_U)
var_sample_U = np.var(sample_U)

#finding pdf of simulated U:
f_sample_U = (1.0/ math.sqrt(2*pi* combined_var))*np.exp((-(sample_U- combined_mu)*2/(2*combined_var)))
    
print("generated new gaussian mean and var are: ", mean_sample_U, "and", var_sample_U )
    
##plotting
plt.scatter(U, f_U, marker =".", color= 'r', label='mathematical')
plt.scatter(sample_U, f_sample_U, marker =".", color= 'cyan', label='simulated')
plt.legend()
plt.xlabel('U')
plt.ylabel('pdf of U: f(U)')
plt.show()  
