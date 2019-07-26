import csv
'''
    date	channel	country	os	impressions	clicks	installs	spend	revenue
'''
with open(sample.csv) as f:
    reader = csv.reader(f)
    for row in reader:
        obj, created = Analyitcs.objects.get_or_create(
            data = row[0],
            channel = row[1],
            country = row[2],
            os = row[3],
            impressions = row[4],
            clicks = row[5],
            installs = row[6],
            spend = row[8],
            revenue = row[9],

        )
        