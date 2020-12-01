import os
import sys
import numpy as np
import Mplot

# Set project include path.
sys.path.append(os.path.join(os.getcwd(),'../'))





######################################################################
#                                                                    #
#							Main function							 #
#                                                                    #
######################################################################

if __name__ == '__main__':
	Mplot.Mp2dDLine('some numbers','x axis','y axis', 'log', [1, 2, 3, 4], [1, 4, 9, 16])

	Mplot.Mp2d2Categories('Categories plotting', ['group_a', 'group_b', 'group_c'], [1, 10, 100])

	Mplot.Mp2dBaloons('Baloons: color=intensity and size=corrolation', 'range',  np.arange(50), 'amplitude', np.arange(50) + 10 * np.random.randn(50),np.random.randint(0, 50, 50), np.random.randn(50) * 100)

	x_grid, y_grid = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
	z_grid = np.sin(np.sqrt(x_grid**2 + y_grid**2))
	Mplot.Mp3DSurface('Mesh plot', x_grid, y_grid, z_grid)

	Mplot.Mp2dHistogram(100, 15, True)




