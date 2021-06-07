import numpy as np
import matplotlib.pyplot as plt

N = 1024 # number of samples to simulate, choose any number you want
x = np.random.randn(N)
plt.figure()
plt.plot(x, '.-')
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Gaussian Noise in time domain")
plt.grid()
plt.show()

X = np.fft.fftshift(np.fft.fft(x))
X = X[N//2:] # only look at positive frequencies.  remember // is just an integer divide
plt.figure()
plt.plot(np.real(X), '.-')
plt.ylabel("Amplitude")
plt.xlabel("Frequency")
plt.title("Gaussian Noise in frequency domain")
plt.grid()

plt.show()


#Complex Noise
n = np.random.randn() + 1j * np.random.randn()
power = np.var(x)
n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # AWGN with unity power
#To plot complex noise in the time domain, like any complex signal we need two lines:

n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2)
plt.figure()
plt.plot(np.real(n),'.-')
plt.plot(np.imag(n),'.-')
plt.legend(['real','imag'])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Complex Gaussian Noise in time domain")
plt.grid()
plt.show()


n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2)
X = np.fft.fftshift(np.fft.fft(n))
X = X[N//2:] # only look at positive frequencies.  remember // is just an integer divide
plt.figure()
plt.plot(np.real(X),'.-')
plt.plot(np.imag(X),'.-')
plt.legend(['real','imag'])
plt.ylabel("Amplitude")
plt.xlabel("Frequency")
plt.title("Complex Gaussian Noise in frequency domain")
plt.grid()
plt.show()

#Complex Gaussian Noise in I-Q Plot
plt.figure()
plt.plot(np.real(n),np.imag(n),'.')
plt.grid(True, which='both')
plt.axis([-2, 2, -2, 2])
plt.xlabel("Q")
plt.ylabel("I")
plt.show()
