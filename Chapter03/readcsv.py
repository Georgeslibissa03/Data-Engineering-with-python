import csv


with open('/home/georgeslibissa/data.csv') as f:
	myreader=csv.DictReader(f)
	headers=next(myreader)
	for row in myreader:
		print(row['name'])
