import math
# print math.factorial(20)
from scipy import stats
#calculating probability from bayes theoram with given 2 equally likely events C1 and c2 
def calcProb_Bayes(P_C1,P_C2,P_A_C1,P_A_C2):
   P_A=P_A_C1*P_C1+P_A_C2*P_C2
   return P_A
#Calculating conditional probalilty given some event has occured
def calcCond_Prob(P_C1,P_A_C1,P_A):
  P_C1_A=(P_A_C1*P_C1)/P_A
  return P_C1_A
# From our question data is given-
P_C1=4/7
P_C2=3/7
P_A_C1=4/10
P_A_C2=5/10
# calculating the probability for event A(Drawn ball is red)
print("Probability such that drawn ball is red from bag 2",calcProb_Bayes(P_C1,P_C2,P_A_C1,P_A_C2))
PA=calcProb_Bayes(P_C1,P_C2,P_A_C1,P_A_C2)
#Probability such that transferred ball is black from bag 1 given drawn ball from bag 2 is red"
print("Probability such that transferred ball is black from bag 1 given drawn ball from bag 2 is red",calcCond_Prob(P_C1,P_A_C1,PA))  
