import numpy as np
import h5py
import scipy.io
import numpy.fft as fft

import matplotlib.pyplot as plt


# f = h5py.File('./Testdata.mat','r')
# data = f.get('data/variable1')
# data = np.array(data)
data = np.array(scipy.io.loadmat('./Testdata.mat')['Undata'])

a = fft.fft(data)
at = fft.fftshift(a)

print(np.size(np.abs(a)))
