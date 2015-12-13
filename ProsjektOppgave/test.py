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


with open('imsiOnlyOnce.csv','rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  temp = []
  for row in spamreader:
    one = float(row[4])
    two = float(row[5])
   
    temp.append([one,two])

  #temp.sort(key=lambda x: x[1])
  X2 = np.array(temp)

  X1 = preprocessing.scale(X2)


classifiers = {
    "Empirical Covariance": EllipticEnvelope(support_fraction=1.,
                                             contamination=0.16),
    "Robust Covariance (Minimum Covariance Determinant)":
    EllipticEnvelope(contamination=0.16),
    "OCSVM": OneClassSVM(nu=0.16, gamma=0.05)}
colors = ['m', 'g', 'b']
legend1 = {}
legend2 = {}


# Learn a frontier for outlier detection with several classifiers
xx1, yy1 = np.meshgrid(np.linspace(-5, 10, 100), np.linspace(-5, 10, 100))
xx2, yy2 = np.meshgrid(np.linspace(-1000, 6000, 2000), np.linspace(-1000, 6000, 2000))
with open('Data/write.txt','wb') as writefile:
  for i, (clf_name, clf) in enumerate(classifiers.items()):

      plt.figure(1)
      clf.fit(X2)
      Z2 = clf.decision_function(np.c_[xx2.ravel(), yy2.ravel()])
      print len(Z2), len(X2)
      writefile.write(clf_name + "\n")
      writefile.write("Decision Function: \n")
      Z2.tofile(writefile,sep=", ")
      Z2 = Z2.reshape(xx2.shape)
      writefile.write("\n Reshape: \n")
      Z2.tofile(writefile, sep=", ")
      writefile.write("\n")
      
      legend2[clf_name] = plt.contour(
          xx2, yy2, Z2, levels=[0], linewidths=2, colors=colors[i])

# Plot the results (= shape of the data points cloud)

legend2_values_list = list( legend2.values() )
legend2_keys_list = list( legend2.keys() )

plt.figure(1)  # "banana" shape
plt.title("Outlier detection uplink/duration vs downlink/duration")
plt.scatter(X2[:, 0], X2[:, 1], color='black')
plt.xlim((-500, 2000))
plt.ylim((-500, 2000))

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