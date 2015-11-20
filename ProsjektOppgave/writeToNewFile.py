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
				if row[0] == '9000' and int(row[-1]) < 500:
					row.pop(0)
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
				if row[0] == '9000' and int(row[-1]) > 500:
					row.pop(0)
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
					
					if counter > 15000:
						spamwriter.writerow(row)

with open('ggsnSample-4Kristofer-hashIMSI.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	#allDnsCalls(spamreader)
	#under500DurationDnsCalls(spamreader)
	#over500DurationDnsCalls(spamreader)
	#first15000DnsCalls(spamreader)
	#restOfDnsCalls(spamreader)