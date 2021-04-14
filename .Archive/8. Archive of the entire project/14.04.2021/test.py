import csv

with open(f'all_probes/0_probe/0_probe.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter=',', quotechar='|')
    i = 1
    for row in csvreader:
        if i == 1:
            print(row)