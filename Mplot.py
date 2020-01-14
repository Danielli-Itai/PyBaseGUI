#Matplot library simple interface functions.
#Check out another optional library:https://seaborn.pydata.org/index.html
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt



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

#Simple categories plotting (category,value pairs).
def Mp2d2Categories(title:str, names:[], values:[], block:bool=False):
	_MpPlot(title)

	plt.plot(names, values)

	plt.bar(names, values)
	plt.scatter(names, values)

	plt.show(block=block)
	return

#Simple colored baloons presenting 4 dimentional data, data is provided as lists.
def Mp2dBaloons(title:str, xlabel:str,x_arr:[], ylabel:str, y_arr:[], color:[], size:[], block:bool=False):
	data = {'xaxis': x_arr, 'yaxis': y_arr, 'color': color, 'size': size}

	_MpPlot(title)

	plt.scatter('xaxis', 'yaxis', c='color', s='size', data=data)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.show(block=block)
	return


# The from import registers for 3D projection, althogh is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
#Simple 3d surface plot on a 3d mesh grid.
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


#Plot a randomly normal distributed histogram.
def Mp2dHistogram(mean, sigma, block:bool=False):
	np.random.seed(19680801)

	# example data
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








"""
This function prints and plots the confusion matrix.
Normalization can be applied by setting `normalize=True`.
"""
import numpy as np  # numpy
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
def plot_confusion_matrix(actual_cls:list, predict_cls:list, classes:list, normalize=False, title=None, cmap=plt.cm.Blues, block:bool=True):
	if not title:
		if normalize:
			title = 'Normalized confusion matrix'
		else:
			title = 'Confusion matrix, without normalization'

	# Compute confusion matrix
	conf_mat = confusion_matrix(actual_cls, predict_cls)

	# Only use the labels that appear in the data
	print("data classes"  +unique_labels(actual_cls, predict_cls))

	if normalize:
		conf_mat = conf_mat.astype('float') / conf_mat.sum(axis=1)[:, np.newaxis]

	fig, axes = plt.subplots()
	axes_img = axes.imshow(conf_mat, interpolation='nearest', cmap=cmap)
	axes.figure.colorbar(axes_img, ax=axes)

	# We want to show all ticks... and label them with the respective list entries
	axes.set(xticks=np.arange(conf_mat.shape[1]), yticks=np.arange(conf_mat.shape[0]), xticklabels=classes, yticklabels=classes,
				title=title, ylabel='True label',  xlabel='Predicted label')

	# Rotate the tick labels and set their alignment.
	plt.setp(axes.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

	# Loop over data dimensions and create text annotations.
	fmt = '.2f' if normalize else 'd'
	thresh = conf_mat.max() / 2.
	for i in range(conf_mat.shape[0]):
		for j in range(conf_mat.shape[1]):
			axes.text(j, i, format(conf_mat[i, j], fmt), ha="center", va="center", color="white" if conf_mat[i, j] > thresh else "black")

	fig.tight_layout()
	plt.show(block=block)
	return axes

