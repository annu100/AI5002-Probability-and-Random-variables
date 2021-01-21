#Define n-no. of trials and p-probability of success
#Define a list of values of r from 0 to n
# mean and variance also calculated
#For verying our results
import matplotlib.pyplot as plt
from scipy.stats import binom 
# setting the values 
# of n and p 
n = 4
p = 0.5
# defining the list of r values 
r_values = list(range(n + 1)) 
# obtaining the mean and variance  
mean, var = binom.stats(n, p) 
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# printing the table 
print("r\tp(r)") 
for i in range(n + 1): 
    print(str(r_values[i]) + "\t" + str(dist[i])) 
# printing mean and variance 
print("mean = "+str(mean)) 
print("variance = "+str(var))
# plotting the graph
plot1=plt.figure(1)
plt.bar(r_values, dist)
dist1 = [binom.cdf(r, n, p) for r in r_values ]# for cdf
plot2=plt.figure(2)
plt.bar(r_values, dist1)
print("for n=4 ,our results got verified\n")
plt.show()
