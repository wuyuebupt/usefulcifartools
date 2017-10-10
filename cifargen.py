import os,sys
import pickle
import numpy as np



if __name__ == '__main__':
	fname = sys.argv[1]
	fo = open(fname, 'rb')
	dic = pickle.load(fo)
	print dic.keys()
	data = dic[b'data']
	label = dic[b'fine_labels']
	print len(data), len(label)
	print data[0]
	print label[0]
		
	mappingfile = sys.argv[2]
	mapping = pickle.load(open(mappingfile))
	print mapping
	usedstart = 0
	usedend = 50

	selected = []
	for i in range(usedstart, usedend):
		# print i
		selected.append(mapping[i])
		
	print selected
	ret = []		
	for i in range(len(data)):
		if label[i] in selected:
			img = data[i].reshape(3,32,32)
			img = np.transpose(img, [1, 2, 0])
			ret.append([img, label[i]])
	
	print len(ret)
	savename = 'cifartop50.p'
	pickle.dump(ret, open(savename,'wb'))

	



