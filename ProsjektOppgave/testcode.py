import csv


dnsimsi = []
dnsimsiWithDuplicate = []
imsi = ''
callDuration = 0 
count = 0 
skip = True
longestCallDuration = 0
aboveAvgDuration = []
underAvgDuration = [9]

with open('ggsnSample-4Kristofer-hashIMSI.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if row[0] == '9000':
		# 	imsi = row[1]b
		# 	dnsimsiWithDuplicate.append(row[1])
		# 	if row[1] not in dnsimsi:
		# 		dnsimsi.append(row[1])
		# if row[1] == imsi:
			callDuration += int(row[6])
			count += 1
			if int(row[6]) > longestCallDuration:
				longestCallDuration = int(row[6])
			if int(row[6]) > 250: #500 = 2403, 250 = 3294
				aboveAvgDuration.append(row)
				print row
			elif int(row[6]) < 250: #500 = 17762, 250 = 16869
				underAvgDuration.append(row)


		#if row[1] == 'ce51a5ec81b36054409277a3b7b9979c':
			#print row
		
			


	# dnsimsi.sort()
	# print len(dnsimsi), len(dnsimsiWithDuplicate)
	avgCallDuration = callDuration/count
	print avgCallDuration, longestCallDuration, (callDuration - longestCallDuration)/(count-1)
	print len(aboveAvgDuration), len(underAvgDuration)
