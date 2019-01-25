import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

L = 20
n = 128

x2 = np.linspace(-L/2, L/2, n+1)
x = x2[0:n-1]

u = np.exp(np.multiply(np.multiply(-1, x), x))
ut = fft.fft(u)
utshift = fft.fftshift(ut)

plt.plot(x,u, label='function, no fft')
plt.plot(np.abs(ut), label='function fft')
plt.plot(np.abs(utshift), label='function fft shifted')

plt.legend()

plt.show()
