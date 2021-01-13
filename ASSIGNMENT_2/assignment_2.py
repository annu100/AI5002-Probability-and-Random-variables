import math
# print math.factorial(20)
from scipy import stats
X = stats.binom(10, 0.05) # Declare X to be a binomial random variable
print("Probability at X=0")
print (X.pmf(0),"\n")          # P(X = 0)
print("Probability at X=1")
print (X.pmf(1),"\n")          # P(X = 1)
print("Probability for getting defective items less than 1")
print (X.cdf(1),"\n")           # P(X <= 1)
