import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy import stats
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn import preprocessing
import time

starttime = time.time()

with open('restOfDnsCalls.csv','rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  temp = []
  for row in spamreader:
    one = float(row[1])
    two = float(row[2])
   
    temp.append([one,two])

  #temp.sort(key=lambda x: x[1])
  X2 = np.array(temp)

  X1 = preprocessing.scale(X2)


classifiers = {
    "Empirical Covariance": EllipticEnvelope(support_fraction=1.,
                                             contamination=0.16),
    "Robust Covariance (Minimum Covariance Determinant)":
    EllipticEnvelope(contamination=0.16),
    "OCSVM": OneClassSVM(nu=0.005, gamma=0.05)}
colors = ['m', 'g', 'b']
legend1 = {}
legend2 = {}


# Learn a frontier for outlier detection with several classifiers
xx1, yy1 = np.meshgrid(np.linspace(-5, 10, 100), np.linspace(-5, 10, 100))
xx2, yy2 = np.meshgrid(np.linspace(-1000, 6000, 1000), np.linspace(-1000, 6000, 1000))
with open('Data/write.txt','wb') as writefile:
  for i, (clf_name, clf) in enumerate(classifiers.items()):
      plt.figure(1)
      clf.fit(X1)
      Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
      print len(Z1), len(X1)
      writefile.write(clf_name + "\n")
      writefile.write("Decision Function: \n")
      Z1.tofile(writefile,sep=", ")
      Z1 = Z1.reshape(xx1.shape)
      writefile.write("\n Reshape: \n")
      Z1.tofile(writefile, sep=", ")
      writefile.write("\n")
      legend1[clf_name] = plt.contour(
          xx1, yy1, Z1, levels=[0], linewidths=2, colors=colors[i])
      plt.figure(2)
      clf.fit(X2)
      Z2 = clf.decision_function(np.c_[xx2.ravel(), yy2.ravel()])
      Z2 = Z2.reshape(xx2.shape)
      
      legend2[clf_name] = plt.contour(
          xx2, yy2, Z2, levels=[0], linewidths=2, colors=colors[i])

legend1_values_list = list( legend1.values() )
legend1_keys_list = list( legend1.keys() )

# Plot the results (= shape of the data points cloud)
plt.figure(1)  # two clusters
plt.title("Outlier detection uplink/duration vs downlink/duration")
plt.scatter(X1[:, 0], X1[:, 1], color='black')
plt.xlim((xx1.min(), xx1.max()))
plt.ylim((yy1.min(), yy1.max()))

plt.legend((legend1_values_list[0].collections[0],
            legend1_values_list[1].collections[0],
            legend1_values_list[2].collections[0]),
           (legend1_keys_list[0], legend1_keys_list[1], legend1_keys_list[2]),
           loc="upper center",
           prop=matplotlib.font_manager.FontProperties(size=12))
plt.ylabel("Uplink/Duration [byte/s]")
plt.xlabel("Downlink/Duration [byte/s]")

#plt.savefig("../rapport/Pictures/scaleUpDivDurVSDownDivDur.png")

legend2_values_list = list( legend2.values() )
legend2_keys_list = list( legend2.keys() )

plt.figure(2)  # "banana" shape
plt.title("Outlier detection uplink/duration vs downlink/duration")
plt.scatter(X2[:, 0], X2[:, 1], color='black')
plt.xlim((-500, 6000))
plt.ylim((-500, 6000))

plt.legend((legend2_values_list[0].collections[0],
            legend2_values_list[1].collections[0],
            legend2_values_list[2].collections[0]),
           (legend2_keys_list[0], legend2_keys_list[1], legend2_keys_list[2]),
           loc="upper center",
           prop=matplotlib.font_manager.FontProperties(size=12))
plt.ylabel("Uplink/Duration [byte/s]")
plt.xlabel("Downlink/Duration [byte/s]")

#plt.savefig("../Rapport/Pictures/unscaledUpDivDurVSDownDivDur.png")
print time.time() - starttime
plt.show()