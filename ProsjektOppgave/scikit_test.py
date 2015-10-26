import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import csv
from scipy import stats

from sklearn import svm
from sklearn.covariance import EllipticEnvelope

with open('clean.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		data.append(row)

	n_samples = len (data)
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

	for i, offset in enumerate(clusters_separation):
		np.random.seed(42)

		X1 = 0.3 * np.random.randn(0.5 * n_inliers, 2) - offset
		X2 = 0.3 * np.random.randn(0.5 * n_inliers, 2) + offset
		X = np.r_[X1, X2]

		X = np.r_[X, np.random.uniform(low=-6, high=6, size=(n_outliers, 2))]
		plt.figure(figsize=(10, 5))
		for i, (clf_name, clf) in enumerate(classifiers.items()):
			# fit the data and tag outliers
		    clf.fit(X)
		    y_pred = clf.decision_function(X).ravel()
		    threshold = stats.scoreatpercentile(y_pred, 100 * outliers_fraction)
		    y_pred = y_pred > threshold
		    n_errors = (y_pred != ground_truth).sum()
		    # plot the levels lines and the points
		    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
		    Z = Z.reshape(xx.shape)
		    subplot = plt.subplot(1, 2, i + 1)
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
		    subplot.set_xlabel("%d. %s (errors: %d)" % (i + 1, clf_name, n_errors))
		    subplot.set_xlim((-7, 7))
		    subplot.set_ylim((-7, 7))
		plt.subplots_adjust(0.04, 0.1, 0.96, 0.94, 0.1, 0.26)

		plt.show()