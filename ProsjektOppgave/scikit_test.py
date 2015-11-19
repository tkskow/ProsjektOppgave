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

	n_samples = len(data)
	outliers_fraction = 0.25
	clusters_separation = [0, 1, 2]

	classifiers = {
	    "One-Class SVM": svm.OneClassSVM(nu=0.95 * outliers_fraction + 0.05, kernel="rbf", gamma=0.1),
	    "robust covariance estimator": EllipticEnvelope(contamination=.1)
	    }

	xx, yy = np.meshgrid(np.linspace(-7, 7, 500), np.linspace(-7, 7, 500))
	n_inliers = int((1. - outliers_fraction) * n_samples)
	n_outliers = int(outliers_fraction * n_samples)
	ground_truth = np.ones(n_samples, dtype=int)
	ground_truth[-n_outliers:] = 0


	#elliptic = EllipticEnvelope(contamination=.1)
	#elliptic.fit(data)
	oneSVM = svm.OneClassSVM()
	oneSVM.fit(data)

with open('restOfDnsCalls.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		data.append([one,two,three])

	
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