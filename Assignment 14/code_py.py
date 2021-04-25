import numpy as np

start = np.array([1,0,0])
start=np.reshape(start,(1,3))
# The transition matrix.
m_3 = np.matrix([
	            [.5,.5,0],
	            [.5,0,.5],
	            [0,0,1]
	            ])

## Probabilities of getting to absorbing state after n tosses.
# First raise the matrix to nth power
# then get the index of absorbing state
p_n = np.array([np.dot(start, np.linalg.matrix_power(m_3,n))
						 [0,2]\
                         for n in range(1,100,2)])#Calculate this upto 100 tosses
#n is odd here
print("Probabilities of getting to absorbing state after n tosses",p_n)
sum_gp=0
print(len(p_n))
#For odd number of tosses
for i in range(len(p_n)):
    sum_gp=sum_gp+p_n[i]
sum_gp=sum_gp/100 #probability it is
print("for 100 tosses ,required probability for getting head for 1st time when number of tosses are odd",sum_gp)
