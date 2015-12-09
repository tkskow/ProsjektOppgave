import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy import stats
import csv
from sklearn import preprocessing

from sklearn import svm
from sklearn.covariance import EllipticEnvelope
with open('imsiOnlyOnce.csv','rb') as csvfile:
#with open('clean.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    temp = []
    for row in spamreader:
        one = float(row[4])
        two = float(row[5])
        #three = float(row[3])
        temp.append([one,two])

    #print temp
    temp.sort(key=lambda x: x[1])
   # print temp
    X1 = np.array(temp)
    X1 = preprocessing.scale(X1)

# Example settings
n_samples = len(temp)
outliers_fraction = 0.05
#clusters_separation = [0, 1, 2]

# define two outlier detection tools to be compared
classifiers = {
    "One-Class SVM": svm.OneClassSVM(nu=0.95 * outliers_fraction + 0.05,
                                     kernel="rbf", gamma=0.5),
    "robust covariance estimator": EllipticEnvelope(contamination=.1)}

# Compare given classifiers under given settings
xx, yy = np.meshgrid(np.linspace(-5, 10, 100), np.linspace(-5, 10, 100))
n_inliers = int((1. - outliers_fraction) * n_samples)
n_outliers = int(outliers_fraction * n_samples)
ground_truth = np.ones(n_samples, dtype=int)
ground_truth[-n_outliers:] = 0


# Fit the problem with varying cluster separation
#for i, offset in enumerate(clusters_separation):

# Fit the model with the One-Class SVM
plt.figure(figsize=(10, 5))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    # fit the data and tag outliers
    clf.fit(X1)
    y_pred = clf.decision_function(X1).ravel()
    threshold = stats.scoreatpercentile(y_pred, 100 * outliers_fraction)
    
    #print y_pred, 100 * outliers_fraction,
    #print threshold
    
    y_pred = y_pred > threshold
    #print y_pred
    n_errors = (y_pred != ground_truth).sum()
    #print n_errors
    # plot the levels lines and the points
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    #print Z, y_pred
    Z = Z.reshape(xx.shape)
    #print Z
    subplot = plt.subplot(1, 2, i + 1)
    subplot.set_title("Outlier detection")
    subplot.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7),
                     cmap=plt.cm.Blues_r)
    a = subplot.contour(xx, yy, Z, levels=[threshold],
                        linewidths=2, colors='red')
    subplot.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                     colors='orange')
    c = subplot.scatter(X1[-n_outliers:, 0], X1[-n_outliers:, 1], c='black')
    b = subplot.scatter(X1[:-n_outliers, 0], X1[:-n_outliers, 1], c='white')
    print len(X1[-n_outliers:]), len (X1[:-n_outliers])
    subplot.axis('tight')
    subplot.legend(
        [a.collections[0], b, c],
        #[a.collections[0], b],
        ['learned decision function', 'true inliers', 'true outliers'],
        prop=matplotlib.font_manager.FontProperties(size=11))
    subplot.set_xlabel("%d. %s (errors: %d)" % (i + 1, clf_name, n_errors))
    subplot.set_xlim((-5, 10))
    subplot.set_ylim((-5, 10))
plt.subplots_adjust(0.04, 0.1, 0.96, 0.94, 0.1, 0.26)

plt.show()