import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import csv
from sklearn import metrics
from scipy import stats
from sklearn import preprocessing

from sklearn import svm
from sklearn.covariance import EllipticEnvelope

with open('first15000DnsCalls.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		for i,x in enumerate(row):
			if i > 0:
				row[i] = float(row[i])
		one = float(row[1])
		two = float(row[2])
		three = float(row[3])
		four = float(row[4])
		five = float(row[5])
		#temp.append([one,two,three])
		#temp.append([one, two])
		temp.append([one,two,three,four,five])

	data = np.array(temp)
	data = preprocessing.scale(data)
	#data = data.
	#elliptic = EllipticEnvelope(contamination=.1)
	#elliptic.fit(data)
	#oneSVM = svm.LinearSVC()
	linear = svm.OneClassSVM(kernel='linear', nu=0.005)
	one16 = svm.OneClassSVM(nu=0.16)
	oneSVM = svm.OneClassSVM(nu=0.005)
	#oneSVM.fit(data[:,4:])
	oneSVM.fit(data)
	linear.fit(data)
	one16.fit(data)


with open('restOfDnsCalls.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		one = float(row[1])
		two = float(row[2])
		three = float(row[3])
		four = float(row[4])
		five = float(row[5])
		#temp.append([one,two,three])
		#temp.append([one, two])
		temp.append([one,two,three,four,five])



	data = np.array(temp)
	data = preprocessing.scale(data)
	#print len(data)
	#for row in data:
	#elliptic.predict(data)
	#print data[:,4:]
	#prediction = oneSVM.predict(data[:,4:])
	prediction5 = oneSVM.predict(data)
	predictionLinear = linear.predict(data)
	prediction16 = one16.predict(data)

	print oneSVM.get_params()
	#print prediction
	negative5 = 0
	positive5 = 0
	negativeL = 0
	positiveL = 0
	negative16 = 0
	positive16 = 0
	for x,i in enumerate(prediction5):
		if prediction5[x] < 0:
			negative5 += 1
			#print data[x,:]
		elif prediction5[x] > 0:
			positive5 += 1
		if predictionLinear[x] < 0:
			negativeL += 1
			#print data[x,:]
		elif predictionLinear[x] > 0:
			positiveL += 1
		if prediction16[x] < 0:
			negative16 += 1
			#print data[x,:]
		elif prediction16[x] > 0:
			positive16 += 1



	print positive5, negative5
	print positive16, negative16
	print positiveL, negativeL

	# for line in data:
	# 	print (oneSVM.decision_function(line[1:]))

	# print oneSVM.decision_function(data[:,1:]).ravel()