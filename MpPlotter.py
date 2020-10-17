##############################################################
# MpPlotter.py
#
# A helper class for creating PieCharts, Scatterplots, and Histographs.
#
# License: MIT 2014 Kevin Peterson
##############################################################
#from BasePy.Config import ConfigCls
import MySQLdb			#import mysql for this library.
from pylab import *
import matplotlib.pyplot as plt
import numpy

sys.path.append(os.path.join(os.getcwd(),'../PyBase'))
from PyBase.Config import ConfigCls





# Pie Chart Statistical graphics
class PieChart:

	# Constractor
	def __init__(self, config:ConfigCls, sql):
		self.config:ConfigCls = config
		self.sql = sql
		self.config = config
# Pie Chart Plot function
	def plot(self, plot_file):

		# Create mysql database connection to get values from tables
		db = MySQLdb.connect(host=self.config.DbHost(), port = int(self.config.DbPort()), user=self.config.DbUser(), password=self.config.DbPassword(), database=self.config.DbName())
		cursor = db.cursor()
		cursor.execute(self.sql)
		result = cursor.fetchall()
		# Plot Dimensions
		ranges = {'0-5':0,'5-10':0,'10-50':0,'50-95':0,'95-100':0}

		for record in result:
			percentage = record[0]
			if 0 <= percentage < 5:
				ranges['0-5'] += 1
			elif 5 <= percentage < 10:
				ranges['5-10'] += 1
			elif 10 <= percentage < 50:
				ranges['10-50'] += 1
			elif 50 <= percentage < 95:
				ranges['50-95'] += 1
			elif 95 <= percentage <= 100:
				ranges['95-100'] += 1
		# Create new presentation figure
		fig = plt.figure()

		# Plot presentation
		plt.pie(ranges.values(), labels=[key + "%" for key in sorted(ranges.keys(), key=lambda key: int(key.split('-')[0]))], autopct=None, shadow=True)

		plt.legend(title="Contribution")

		F = gcf()
		# Save plot as png image
		F.savefig(self.config.PlotsDir() + plot_file + ".png")
		plt.close(fig)




# Scatter Plot  Statistical graphics
class ScatterPlot:
	#Constractor
	def __init__(self, config:ConfigCls, sql, xlabel, ylabel, xrange=None, yrange=None):
		self.config:ConfigCls = config
		self.sql = sql
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.xrange = xrange
		self.yrange = yrange

	# Scatter Plot  function
	def plot(self, plot_file:str):
		# Create mysql database connection to get values from tables
		db = MySQLdb.connect(host=self.config.DbHost(), port = int(self.config.DbPort()), user=self.config.DbUser(), password=self.config.DbPassword(), database=self.config.DbName())
		cursor = db.cursor()
		cursor.execute(self.sql)
		result = cursor.fetchall()

		x = []
		y = []

		# Storged  mysql database cursor result in two arrays
		for record in result:
			x.append(record[0])
			y.append(record[1])

		# Create new presentation figure
		fig = plt.figure() 
		m,b = numpy.polyfit(x,y,1)

		plt.scatter(x,y)

		correlation_coefficient = "%.4f" % numpy.corrcoef(x,y)[0,1]
		title('Correlation Coefficient: ' + correlation_coefficient, fontsize=18)

		# Plot presentation
		if float(correlation_coefficient) > 0.5:
			plt.plot(x,y,'bo',x,m*numpy.array(x)+b,'-k',linewidth=2)

		plt.xlabel(self.xlabel,fontsize=18)
		plt.ylabel(self.ylabel,fontsize=18)
		plt.xlim(self.xrange)
		plt.ylim(self.yrange)
		# Save plot as png image
		F = gcf()
		F.savefig(self.config.PlotsDir() + plot_file + ".png")
		plt.close(fig)

		f = open(self.config.OutDir() + plot_file + "-correlation.tex",'w')
		f.write(str(correlation_coefficient))
		f.close()




# Histograph Statistical graphics
class Histograph:
	#Constractor
	def __init__(self, config:ConfigCls, sql_query, xlabel, ylabel, range=None):
		self.config = config
		self.sql_query = sql_query
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.range = range
	# Histograph plot function
	def plot(self, plot_file):
		# Create mysql database connection to get values from tables
		db = MySQLdb.connect(host=self.config.DbHost(), port = int(self.config.DbPort()), user=self.config.DbUser(), password=self.config.DbPassword(), database=self.config.DbName())
		cursor = db.cursor()

		cursor.execute(self.sql_query)

		result = cursor.fetchall()

		x = []
		# Storged  mysql database cursor result in an array
		for record in result:
		  x.append(record[0])

		# Create new  presentation figure
		fig = plt.figure() 
		plt.hist(x, range=self.range)
		plt.xlabel(self.xlabel,fontsize=18)
		plt.ylabel(self.ylabel,fontsize=18)

		# Save plot as png image
		F = gcf()
		F.savefig(self.config.PlotsDir() + plot_file + ".png")
		plt.close(fig)