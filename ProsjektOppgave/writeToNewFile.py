import csv
first = True


def allDnsCalls(csvIn):
	with open('allDnsCalls.csv', 'wb') as writefile:
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')
		for row in csvIn:
				row.pop(-1)
				row.pop(-2)
				row.pop(-2)
	#			if first:
	#				spamwriter.writerow(row)
	#				first = False
				if row[0] == '9000':
					row.pop(0)
					if float(row[-1]) == 0:
						bpsUp = row[1]
						bpsDown = row[2]
					else:
						bpsUp = float(row[1])/float(row[-1])
						bpsDown = float(row[2])/float(row[-1])
					
					row.append(bpsUp)
					row.append(bpsDown)
					spamwriter.writerow(row)

def under500DurationDnsCalls(csvIn):
	with open('under500DurationDnsCalls.csv', 'wb') as writefile:
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')
		for row in csvIn:
				row.pop(-1)
				row.pop(-2)
				row.pop(-2)
	#			if first:
	#				spamwriter.writerow(row)
	#				first = False
				if row[0] == '9000' and float(row[-1]) < 500:
					row.pop(0)
					if float(row[-1]) == 0:
						bpsUp = row[1]
						bpsDown = row[2]
					else:
						bpsUp = float(row[1])/float(row[-1])
						bpsDown = float(row[2])/float(row[-1])
					
					row.append(bpsUp)
					row.append(bpsDown)
					spamwriter.writerow(row)

def over500DurationDnsCalls(csvIn):
	with open('over500DurationDnsCalls.csv', 'wb') as writefile:
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')
		for row in csvIn:
				row.pop(-1)
				row.pop(-2)
				row.pop(-2)
	#			if first:
	#				spamwriter.writerow(row)
	#				first = False
				if row[0] == '9000' and float(row[-1]) > 500:
					row.pop(0)
					if float(row[-1]) == 0:
						bpsUp = row[1]
						bpsDown = row[2]
					else:
						bpsUp = float(row[1])/float(row[-1])
						bpsDown = float(row[2])/float(row[-1])
					
					row.append(bpsUp)
					row.append(bpsDown)
					spamwriter.writerow(row)

def first15000DnsCalls(csvIn):
	with open('first15000DnsCalls.csv', 'wb') as writefile:
		counter = 0 
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')
		for row in csvIn:
				row.pop(-1)
				row.pop(-2)
				row.pop(-2)
	#			if first:
	#				spamwriter.writerow(row)
	#				first = False
				if row[0] == '9000':
					counter += 1
					row.pop(0)
					if float(row[-1]) == 0:
						bpsUp = row[1]
						bpsDown = row[2]
					else:
						bpsUp = float(row[1])/float(row[-1])
						bpsDown = float(row[2])/float(row[-1])
					
					row.append(bpsUp)
					row.append(bpsDown)
					spamwriter.writerow(row)
					if counter > 15000:
						break

def restOfDnsCalls(csvIn):
	with open('restOfDnsCalls.csv', 'wb') as writefile:
		counter = 0 
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')
		for row in csvIn:
				row.pop(-1)
				row.pop(-2)
				row.pop(-2)
	#			if first:
	#				spamwriter.writerow(row)
	#				first = False
				if row[0] == '9000':
					counter += 1
					row.pop(0)
					if float(row[-1]) == 0:
						bpsUp = row[1]
						bpsDown = row[2]
					else:
						bpsUp = float(row[1])/float(row[-1])
						bpsDown = float(row[2])/float(row[-1])
					
					row.append(bpsUp)
					row.append(bpsDown)
					
					if counter > 15000:
						spamwriter.writerow(row)


def smallSetToTest(csvIn):
	with open('smallSetToTest.csv', 'wb') as writefile:
		counter = 0 
		spamwriter = csv.writer(writefile, delimiter=',', quotechar='|')
		for row in csvIn:
				row.pop(-1)
				row.pop(-2)
				row.pop(-2)
	#			if first:
	#				spamwriter.writerow(row)
	#				first = False
				if row[0] == '9000':
					counter += 1
					row.pop(0)
					if float(row[-1]) == 0:
						bpsUp = row[1]
						bpsDown = row[2]
					else:
						bpsUp = float(row[1])/float(row[-1])
						bpsDown = float(row[2])/float(row[-1])
					
					row.append(bpsUp)
					row.append(bpsDown)
					spamwriter.writerow(row)
					if counter > 150:
						break

with open('ggsnSample-4Kristofer-hashIMSI.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	#allDnsCalls(spamreader)
	#under500DurationDnsCalls(spamreader)
	#over500DurationDnsCalls(spamreader)
	#first15000DnsCalls(spamreader)
	#restOfDnsCalls(spamreader)
	smallSetToTest(spamreader)