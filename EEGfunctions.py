import numpy as np
import cPickle
import matplotlib.pyplot as plt


def plot_EEG(X):
	"""
	Input shape: (T,N), T~10000. N=14.
	"""
	for i in range(X.shape[1]):
	    plt.plot(np.arange(X.shape[0]),X[:,i])
	    plt.title("Trajectory of EEG signal")
	    plt.xlabel("Time step")
	    plt.ylabel("EEG values")
	    plt.show()