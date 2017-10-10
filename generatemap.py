import os,sys
import pickle


if __name__ == '__main__':
	lines = open(sys.argv[1])
	count = 0
	mapping = {}
	mappingcifarkey = {}
	for line in lines:
		arr = line.strip().split()
	print len(arr), arr
	for i in arr:
		mappingcifarkey[int(i)] = count
		mapping[count] = int(i)
		count += 1
	pickle.dump(mapping, open('mapping.p', 'wb'))
	pickle.dump(mappingcifarkey, open('mappingcifarkey.p', 'wb'))
