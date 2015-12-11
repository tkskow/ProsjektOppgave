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
    #"linear nu = 0.005": OneClassSVM(kernel='linear', nu=0.005),
    "nu = 0.15": OneClassSVM(nu=0.15),
    "nu = 0.25": OneClassSVM(kernel='rbf', nu=0.25),
    "nu = 0.05": OneClassSVM(nu=0.05),
    "nu = 0.005": OneClassSVM(nu=0.005)}
colors = ['m', 'g', 'b', 'y']
legend1 = {}


# Learn a frontier for outlier detection with several classifiers
xx1, yy1 = np.meshgrid(np.linspace(-5, 20, 200), np.linspace(-5, 20, 200))
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
            legend1_values_list[2].collections[0],
            legend1_values_list[3].collections[0]),
           (legend1_keys_list[0], legend1_keys_list[1], legend1_keys_list[2], legend1_keys_list[3]),
           #(legend1_keys_list[0], legend1_keys_list[1]),
           loc="upper center",
           prop=matplotlib.font_manager.FontProperties(size=12))
plt.ylabel("Uplink/Duration [byte/s]")
plt.xlabel("Downlink/Duration [byte/s]")

plt.savefig("../rapport/figs/imsiDifferentNu.png")

print time.time() - starttime
plt.show()