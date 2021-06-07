import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

gamma_ratio_dB = np.arange(start=-10,stop=40,step=2)
Ns = [1,2,3,4,10,20] #number of received signal paths

gamma_ratio = 10**(gamma_ratio_dB/10) #Average SNR/SNR threshold in dB

fig, ax = plt.subplots(1, 1)

for N in Ns:
        n = np.arange(start=0,stop=N,step=1)
        P_outage = 1 - np.exp(-1/gamma_ratio)*np.sum(((1/gamma_ratio)**n[:,None])/factorial(n[:,None]),axis=0)
        ax.semilogy(gamma_ratio_dB,P_outage,label='N='+str(N))

ax.legend()
ax.set_xlim(-10,40);ax.set_ylim(0.0001,1.1)
ax.set_title('MRC outage probability (Rayleigh fading channel)')
ax.set_xlabel(r'$10log_{10}\left(\Gamma/\gamma_t\right)$')
ax.set_ylabel('Outage probability');fig.show()
