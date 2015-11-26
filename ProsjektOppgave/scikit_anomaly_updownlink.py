from sklearn import svm
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy import stats



with open('smallSetToTest.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	temp = []
	for row in spamreader:
		one = float(row[4])
		two = float(row[5])
		temp.append([one,two])

	data = np.array(temp)
	clf = svm.OneClassSVM(kernel='rbf',nu=0.16)
	clf.fit(data)


xx, yy = np.meshgrid(np.linspace(-100, 1000, 1000), np.linspace(-100, 1000, 1000))
n_outliers = 0.16

with open('smallSetToTest.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = float(row[4])
		two = float(row[5])
		data.append([one,two])

	X = np.array(data)
	y_pred = clf.decision_function(X).ravel()
	threshold = stats.scoreatpercentile(y_pred, 100 * n_outliers)
	Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
	Z = Z.reshape(xx.shape)
	subplot = plt.subplot(1, 1, 0 + 1)
	subplot.set_title("Outlier detection")
	subplot.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7), cmap=plt.cm.Blues_r)
	a = subplot.contour(xx, yy, Z, levels=[threshold], linewidths=2, colors='red')
	subplot.contourf(xx, yy, Z, levels=[threshold, Z.max()], colors='orange')
	b = subplot.scatter(X[:-n_outliers, 0], X[:-n_outliers, 1], c='white')
	c = subplot.scatter(X[-n_outliers:, 0], X[-n_outliers:, 1], c='black')
	subplot.axis('tight')
	subplot.legend(
		[a.collections[0], b, c],
		['learned decision function', 'true inliers', 'true outliers'],
		prop=matplotlib.font_manager.FontProperties(size=11))
	#subplot.set_xlabel("%d. %s (errors: %d)" % (0 + 1))
	subplot.set_xlim((-500, 6000))
	subplot.set_ylim((-500, 6000))
	plt.subplots_adjust(0.04, 0.1, 0.96, 0.94, 0.1, 0.26)

plt.show()