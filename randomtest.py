import os,sys
import numpy as np

if __name__ == '__main__':
	np.random.seed(1993)
	order = np.arange(100)
	np.random.shuffle(order)
	np.save('order', order)
	print order
	print order[0:50]
