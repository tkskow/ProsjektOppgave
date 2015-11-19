from sklearn import svm
import csv



with open('first15000DnsCalls.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		data.append([one,two,three])

	clf = svm.OneClassSVM(kernel='linear',nu=0.16)
	clf.fit(data)

with open('restOfDnsCalls.csv','rb') as csvfile2:
	spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
	data = []
	for row in spamreader:
		one = int(row[1])
		two = int(row[2])
		three = int(row[3])
		data.append([one,two,three])

	
	prediction = clf.predict(data)
	negative = 0
	positive = 0
	for i in prediction:
		if i < 0:
			negative += 1
		else:
			positive += 1
	print positive, negative