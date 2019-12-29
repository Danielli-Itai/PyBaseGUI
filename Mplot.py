#Matplot library simple interface functions.
#Check out another optional library:https://seaborn.pydata.org/index.html

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


#Create a new plot.
def _MpPlot(title:str)->plt.figure:
	fig = plt.figure()
	plt.suptitle(title)
	return(fig)


#Simple line plot 'logit', 'symlog', 'log', 'linear'
def Mp2dDLine(title:str, xlable:str, ylable:str, yscale:str, indxx:[], arr:[], block:bool=False):
	_MpPlot(title)
	plt.plot(indxx, arr, 'ro')

	plt.xlabel(xlable)
	plt.ylabel(ylable)

	plt.yscale(yscale)

	plt.show(block=block)
	return

#Simple categories plotting.
def Mp2d2Categories(title:str, names:[], values:[], block:bool=False):
	_MpPlot(title)

	plt.plot(names, values)

	plt.bar(names, values)
	plt.scatter(names, values)

	plt.show(block=block)
	return

#Simple colored baloons whaere data is provided as array.
def Mp2dBaloons(title:str, xlabel:str,x_arr:[], ylabel:str, y_arr:[], color:[], size:[], block:bool=False):
	data = {'xaxis': x_arr, 'yaxis': y_arr,
	        'color': color, 'size': size}

	_MpPlot(title)

	plt.scatter('xaxis', 'yaxis', c='color', s='size', data=data)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.show(block=block)
	return


def Mp2dHistogram(mean, sigma, block:bool=False):
	np.random.seed(19680801)

	# example data
#	mean = 100  # mean of distribution
#sigma = 15  # standard deviation of distribution
	x = mean + sigma * np.random.randn(437)

	num_bins = 50

	fig, ax = plt.subplots()

	# the histogram of the data
	n, bins, patches = ax.hist(x, num_bins, density=1)

	# add a 'best fit' line
	y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	     np.exp(-0.5 * (1 / sigma * (bins - mean)) ** 2))
	ax.plot(bins, y, '--')
	ax.set_xlabel('Smarts')
	ax.set_ylabel('Probability density')
	ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

	# Tweak spacing to prevent clipping of ylabel
	fig.tight_layout()
	plt.show(block=block)
	return

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
def Mp3DSurface(title:str, X:[[]], Y:[[]], Z:[[]], block:bool=False):
	fig = _MpPlot(title)
	ax = fig.gca(projection='3d')

	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)  #@UndefinedVariable
	ax.set_zlim(-1.01, 1.01)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	fig.colorbar(surf, shrink=0.5, aspect=5)

	plt.show(block=block)
	return
