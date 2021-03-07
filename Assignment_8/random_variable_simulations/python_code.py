import numpy as np
import random
from matplotlib import pyplot as plt
# import uniform distribution
from scipy.stats import uniform
#num_trials is sample size
# p is 2 length vector containing probabilities(pmf)
# X is random variable which has 3 outcomes
#Please note here,X=0 represents P(A),X=1 represents P(B)
p=[7/13,9/13]
num_trials=int(input("Enter number of samples to be printed a/c to pmf\n"))#global variable
cdfp=[0,0]
cdfp=np.cumsum(p)# Cummulative pdf of pmf given
#print(cdfp)
def randomsamples(num_trials,p):
 Samples=[x for x in range(num_trials)]# creating string array for storage of samples
 alpha=["0","1"]
 for i in range(num_trials):
      U=np.random.rand() #random number between 0 and 1
      if (U<=cdfp[0]):
         Samples[i]=alpha[0]
      elif (U>cdfp[0]):
         Samples[i]=alpha[1]
       
    

      
 Samples=str(Samples)
 return(Samples)
y=randomsamples(num_trials,p)
print("Generated samples according to the probability distribution is \n")
print(y)
count0=y.count("0")
count1=y.count("1")

print(count0)
print(count1)

print("simulation versus actual probabilities")
print("Actual probabilities i.e P(A),P(B)are",p)
print("simulation probabilities are given by \n")
p_simul=[count0/num_trials,count1/num_trials]
print("Probability for X=0 i.e P(A)is ",count0/num_trials)
print("Probability for X=1 i.e P(B)is ",count1/num_trials)

plt.plot(p,p_simul,marker="o",color="red")
plt.xlabel("Actual probability")
plt.ylabel("probability after simulation of random variables")
plt.title("simulation versus actual probabilities")
#Using baye's theoram,P(A/B)=P(AB)/P(B)
#HERE P(A/B)=P(2)/P(1)
required_prob_simulation=(4/13)/p_simul[1]
required_prob_calcu_bayes=(4/13)/p[1]
print("simulation versus actual probabilities for P(A/B)")
print("simulated prob is i.e P(A/B)",required_prob_simulation)
print("using baye''s probabilities i.e P(A/B)is \n",required_prob_calcu_bayes)

plt.show()
