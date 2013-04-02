from Pycluster import kcluster
from math import sqrt
import sys

import csv

NCLUSTERS = 3

data = []

with open('output.csv', 'rUb') as csvfile:
	reader = csv.reader(csvfile, delimiter=';')
	for row in reader:
		if reader.line_num == 1:
			continue
		# if reader.line_num == 10000:
		# 	break
		data.append([int(item) for item in row])

print data[0]
labels = ['N' if row[-1] == 0 else 'A' for row in data]

average = [0] * len(data[0])
std = [0] * len(data[0])


for row in data:
	for i, item in enumerate(row):
		average[i] += item

average = [float(i) / len(data) for i in average]

for row in data:
	for i, item in enumerate(row):
		std[i] += (item - average[i]) ** 2

std = [sqrt(float(i) / (len(data) - 1)) for i in std]
print average
print std

for i in xrange(len(data)):
	for j in xrange(len(data[0])):
		data[i][j] = (data[i][j] - average[j]) / std[j]

print data[0]


clusterid, error, nfound = kcluster(data, nclusters=NCLUSTERS, npass=20)
print clusterid, error, nfound

# output_file = open('output.log', 'w')
# for i in xrange(len(labels)):
# 	output_file.write(labels[i] + ' ' + str(clusterid[i]))

attacks_per_cluster = [0] * NCLUSTERS
normal_per_cluster = [0] * NCLUSTERS

for i in xrange(len(labels)):
	if labels[i] == 'A':
		attacks_per_cluster[clusterid[i]] += 1
	else:
		normal_per_cluster[clusterid[i]] += 1

print "Attacks"
print ['%4d' % (item,) for item in attacks_per_cluster]
print "Normal"
print ['%4d' % (item,) for item in normal_per_cluster]