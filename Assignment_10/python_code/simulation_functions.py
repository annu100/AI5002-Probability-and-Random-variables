# A Python program to print all  
# permutations of given length  

from itertools import permutations  
import numpy as np
import random
import matplotlib.pyplot as plt
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
randomlist=np.append(randomlist,20)
print("Random list is:")
print(randomlist) 
# Get all permutations of length 20  
# and length 2  
#X=np.random.randint(20)
perm = permutations(randomlist, 2)  

  
# Print the obtained permutations  
print("possible permutations when no. of elements varies between 10 to 30")
x=np.array([])
y=np.array([])
for i in list(perm):
    w,v=i
    x=np.append(x,w)
    y=np.append(y,v)
    print(i)
    
#when number of elements is 20
success=20*19  #total one to one functions
possible_outcomes=20*20
prob=success/possible_outcomes
print(x)
print(y)
plt.figure(1)

plt.scatter(x,y)
plt.title("possible permutations of one to one functions when size of X varies")
plt.xlabel("variable lengths")
plt.ylabel("possible permutations")
plt.show()










