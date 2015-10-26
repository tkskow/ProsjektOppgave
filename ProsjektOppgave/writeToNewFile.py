import csv
first = True

with open('ggsnSample-4Kristofer-hashIMSI.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	with open('clean.csv', 'wb') as writefile:
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')

		for row in spamreader:
			row.pop(-1)
			row.pop(-2)
			row.pop(-2)
#			if first:
#				spamwriter.writerow(row)
#				first = False
			if row[0] == '9000':
				row.pop(0)
				spamwriter.writerow(row)
