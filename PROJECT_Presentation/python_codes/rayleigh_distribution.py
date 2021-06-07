#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss

gamma_dB = np.linspace(0, 45, 15)

def Pe(x):
    return 0.5 - 0.5*(math.sqrt(x/(2+x)))

vect_Pe = []

#simulation
simlen = int(1e6)
N = np.random.normal(0,1,simlen)

prob = []

for i in range(0, 15):

  gamma = 10**(0.1*gamma_dB[i])
  
  A=ss.rayleigh.rvs( loc = 0, scale = math.sqrt((gamma)/2),size=simlen)
  prob_sum = 0
  for j in range(simlen):
    if A[j]+N[j]<0:
      prob_sum=prob_sum+1
        
  prob_sum /= simlen
  prob.append(prob_sum)
  vect_Pe.append(Pe(gamma))


plt.semilogy(gamma_dB.T, vect_Pe, '-')
plt.semilogy(gamma_dB.T, prob, 'o')
plt.xlabel('SNR in dB')
plt.ylabel('$P_e$')
plt.legend(["Rayleigh Theoretical", "Simulated"])
plt.grid()
plt.show() #opening the plot window

###############
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

def qfunc(x):
	return 0.5*mp.erfc(x/mp.sqrt(2))

 
snrlen = 13
snrdb = np.linspace(0,13,13)
simlen = int(1e5)
#Simulated BER declaration
err = []
#Analytical BER declaration
ber = []

#for SNR 0 to 10 dB
for i in range(0,snrlen):
	awgn = np.random.normal(0,1,simlen)
	snr = 10**(0.1*snrdb[i])
	rx = mp.sqrt(snr) + awgn
	err_ind = np.nonzero(rx < 0)#condition for a misinterpreted bit
	#calculating the total number of errors
	err_n = np.size(err_ind)
	#calcuating the simulated BER
	err.append(err_n/simlen)
	#calculating the analytical BER
	ber.append(qfunc(mp.sqrt(snr)))
	
plt.semilogy(snrdb.T,ber,label='AWGN theory')
plt.semilogy(snrdb.T,err,'o',label='Simulated')
plt.xlabel('SNR in dB')
plt.ylabel('$P_B$')
plt.legend()
plt.grid()
plt.show()
#print(qfunc(mp.sqrt(10**(0.1*1))))

##############
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss

simlen = int(1e5)	
x = np.linspace(0,15,simlen)
A=ss.rayleigh.pdf(x, loc=0, scale=1)
B=ss.rayleigh.pdf(x, loc=0, scale=2)
C=ss.rayleigh.pdf(x, loc=0, scale=3)
D=ss.rayleigh.pdf(x, loc=0, scale=4)

plt.plot(x,A)
plt.plot(x,B)
plt.plot(x,C)
plt.plot(x,D)

plt.legend(["$\sigma$=1","$\sigma$=2","$\sigma$=3","$\sigma$=4"], loc ="upper right")
