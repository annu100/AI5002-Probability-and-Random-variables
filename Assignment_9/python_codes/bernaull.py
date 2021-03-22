import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import math
from scipy import stats

# From our question data is given-
#Can be interpreted as bernaulli random variable
P_A=1/13
P_B=12/13

print("Probability such that ace we get(actual)",P_A)
print("Probability such that ace we do not get(actual)",P_B)


def simulate_bayes_bernoulli():
   
    
    sim_len = int(1e4)
    
    sim_bern1 = bernoulli.rvs(size=sim_len, p=P_A)
    sim_bern2 = bernoulli.rvs(size=sim_len, p=P_B)
    
    fav_drawn = np.nonzero(sim_bern1 == 1)
    fav_transfer = np.nonzero(sim_bern2 == 1)
    
    p_sim_bern1 = len(fav_drawn[0])/sim_bern1.size
    p_sim_bern2 = len(fav_transfer[0])/sim_bern2.size
    
    plt.figure()
    plot(sim_bern1,
      'calculating the probability for event A',
      'Simulation of Bernoulli Distribution for getting an ace')
    print('\n Simulation P( calculating the probability for event= %f\n' % p_sim_bern1)
    print('\n ACTUAL P( calculating the probability for event A)= %f\n' % P_A)
    print('\n Simulation P( Probability for not getting ace  is ) = %f\n' % p_sim_bern2)
    print('\n ACTUAL P(Not getting ace)= %f\n' % P_B)
    plt.figure()
    plot(sim_bern2, 
      'calculating the probability for event B',
      'Simulation of Bernoulli Distribution for not getting an ace')

def plot(data_bern, xl, t):
    ax = sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={'linewidth': 25,'alpha':1})
    ax.set(xlabel=xl, ylabel='Frequency')
    ax.set(title=t)
    plt.show()


simulate_bayes_bernoulli()
