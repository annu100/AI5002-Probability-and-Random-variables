from matplotlib import pyplot as plt
sides=6; # 2 dices with 6 sides
def all_rolls(sides):
    """Return sum of all combinations of two dice with given number of sides."""
    result = []
    temp_list = list(range(2, 2*sides+1))

    while temp_list:
        result.extend(temp_list)
        temp_list = temp_list[1:-1]

    return sorted(result)
y=all_rolls(6) # returns all combinations of sum of numbers on 2 dices
possible_outcomes=36 # total number of outcomes
print(y)
occurance=[x for x in range(11)] 
prob=[x for x in range(11)]
def find_prob(y):
  x=[2,3,4,5,6,7,8,9,10,11,12]
  for i in range(11):
     occurance[i]=y.count(x[i]) # counting each outcome
     prob[i]=occurance[i]/possible_outcomes; #desired probability matrix
  return prob
print("probability for getting sum on 2 dices are given by:",find_prob(y))
x=[2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x,find_prob(y),marker='o')
plt.xlabel("possible sums of 2 numbers appearing on two dices")
plt.ylabel("probability of sum of 2 numbers appearing on two dices")
plt.title("graph of probability versus sum of two numbers")
plt.show()
