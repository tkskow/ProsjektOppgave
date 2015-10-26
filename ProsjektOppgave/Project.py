import csv

imsi = ''
counter = 0
downLink = 0 
upLink = 0
with open('ggsnSample-4Kristofer-hashIMSI.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if row[0] == '9000':
			#print row
			row.pop(-1)
			row.pop(-2)
			row.pop(-2)
			row.pop(0)
			print row
		# 	imsi = row[1]
		# 	if row[-1] != '4000':
		# 		print row
			
		# counter += 1
			#downLink += int(row[3])
			#upLink += int(row [2])

	#avgDownLink = downLink/counter
	#avgUpLink = upLink/counter

	#print avgUpLink,avgDownLink #711, 1590
	#print counter #20167
		# if row[1] == imsi:
		# 	print row
