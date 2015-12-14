import csv
import numpy as np
import matplotlib.pyplot as plt





def fullDataset():
	dnsimsi = []
	dnsimsiWithDuplicate = []
	imsi = ''
	skip = True
	callDuration = 0 
	count = 0 
	longestCallDuration = 0
	aboveAvgDuration = []
	underAvgDuration = []
	allrows = []
	uplink = []
	downlink = []
	duration = []
	with open('ggsnSample-4Kristofer-hashIMSI.csv','rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			if row[0] == '9000':
			# 	imsi = row[1]b
			# 	dnsimsiWithDuplicate.append(row[1])
			# 	if row[1] not in dnsimsi:
			# 		dnsimsi.append(row[1])
			# if row[1] == imsi:
				row[2] = int(row[2])
				row[6] = int(row[6])
				row[3] = int(row[3])
				callDuration += int(row[6])
				count += 1
				allrows.append(row)
				uplink.append(int(row[2]))
				downlink.append(int(row[3]))
				duration.append(int(row[6]))
				if int(row[6]) > longestCallDuration:
					longestCallDuration = int(row[6])
				if int(row[6]) > 250: #500 = 2403, 250 = 3294
					aboveAvgDuration.append(row)
					#print row
				elif int(row[6]) < 250: #500 = 17762, 250 = 16869
					underAvgDuration.append(row)


			#if row[1] == 'ce51a5ec81b36054409277a3b7b9979c':
				#print row
			
				
		histoUP, bin = np.histogram(uplink, bins=1000)
		allcalls = np.array(allrows)
		# dnsimsi.sort()
		# print len(dnsimsi), len(dnsimsiWithDuplicate)
		avgCallDuration = callDuration/count
		#print uplink
		print avgCallDuration, longestCallDuration, (callDuration - longestCallDuration)/(count-1)
		print len(aboveAvgDuration), len(underAvgDuration)
		print float(len(aboveAvgDuration))/count, float(len(underAvgDuration))/count
		print min(uplink), max(uplink), min(downlink), max(downlink)
		print histoUP
		plt.bar(bin[:-1], histoUP, width=1)
		plt.ylim(0,50)
		plt.show()


def first15000():
	callDuration = 0 
	count = 0 
	longestCallDuration = 0
	aboveAvgDuration = []
	underAvgDuration = []
	with open ('first15000DnsCalls.csv','rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			callDuration += int(row[-1])
			count += 1
			if int(row[-1]) > longestCallDuration:
				longestCallDuration = int(row[-1])
			if int(row[-1]) > 250: #500 = 2403, 250 = 3294
				aboveAvgDuration.append(row)
				#print row
			elif int(row[-1]) < 250: #500 = 17762, 250 = 16869
				underAvgDuration.append(row)
	print callDuration/count, float(len(aboveAvgDuration))/count, float(len(underAvgDuration))/count



fullDataset()
#first15000()