import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import csv
from scipy import stats

from sklearn import svm
from sklearn.covariance import EllipticEnvelope

with open('first15000DnsCalls.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		data.append([one,two,three])



	#elliptic = EllipticEnvelope(contamination=.1)
	#elliptic.fit(data)
	oneSVM = svm.OneClassSVM(nu=0.16)
	oneSVM.fit(data)

with open('restOfDnsCalls.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		data.append([one,two,three])

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


with open('restOfDnsCalls.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		data.append([one,two,three])

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
	