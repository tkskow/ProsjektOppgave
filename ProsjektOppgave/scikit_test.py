import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import csv
from scipy import stats

from sklearn import svm
from sklearn.covariance import EllipticEnvelope

with open('first15000DnsCalls.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		temp.append([one,two,three])



	#elliptic = EllipticEnvelope(contamination=.1)
	#elliptic.fit(data)
	oneSVM = svm.LinearSVC()
	#oneSVM = svm.OneClassSVM(nu=0.16)
	oneSVM.fit(temp)

with open('restOfDnsCalls.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		temp.append([one,two,three])
	data = np.array(temp)
	print len(data)	
	#for row in data:
	#elliptic.predict(data)
	prediction = oneSVM.predict(data)
	negative = 0
	positive = 0
	for i in prediction:
		if i < 0:
			negative += 1
		else:
			positive += 1
	print positive, negative

	print oneSVM.decision_function(data)