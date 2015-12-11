import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import csv
from sklearn import metrics
from scipy import stats
from sklearn import preprocessing

from sklearn import svm
from sklearn.covariance import EllipticEnvelope

with open('imsiOnlyOnceTrain.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		for i,x in enumerate(row):
			if i > 0:
				row[i] = float(row[i])
		one = float(row[1])
		two = float(row[2])
		three = float(row[3])
		temp.append([one,two,three])
		#temp.append(row)

	data = np.array(temp)
	data = preprocessing.scale(data)
	#data = data.
	#elliptic = EllipticEnvelope(contamination=.1)
	#elliptic.fit(data)
	#oneSVM = svm.LinearSVC()
	oneSVM = svm.OneClassSVM(nu=0.005)
	#oneSVM.fit(data[:,4:])
	oneSVM.fit(data)


with open('imsiOnlyOnceTest.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		row[4] = float(row[1])
		row[5] = float(row[2])
		#print type(one)
		three = float(row[3])
		temp.append([one,two,three])
		#temp.append(row)
		#data = np.array(temp)



	data = np.array(temp)
	data = preprocessing.scale(data)
	#print len(data)
	#for row in data:
	#elliptic.predict(data)
	#print data[:,4:]
	#prediction = oneSVM.predict(data[:,4:])
	prediction = oneSVM.predict(data)

	print oneSVM.get_params()
	print prediction
	negative = 0
	positive = 0
	for x,i in enumerate(prediction):
		if i < 0:
			negative += 1
			#print data[x,:]
		else:
			positive += 1
	print positive, negative

	# for line in data:
	# 	print (oneSVM.decision_function(line[1:]))

	# print oneSVM.decision_function(data[:,1:]).ravel()