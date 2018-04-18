import argparse
import sys
import random

def data_read(file):
	'''
	Reads the data from the text file and returns as
	list of lists
	'''
	data_points = []
	with open(file,'r') as f:
		data_points = f.readlines()

	for i,lines in enumerate(data_points):
		data_points[i] = lines.split()

	for points in data_points:
		for i,point in enumerate(points):
			points[i] = float(point)
	# print(data_points)

	return data_points

def k_means(data_points, k):
	'''
	Implements K-means clustering algorithm and stores the 
	number of clusters specified in the clusters.txt file
	'''
	centroids = []
	for i in range(k):
		centroids[i] = random.choice(data_points)

	print(centroids)


def main():
	'''
	Main program which runs and takes care of 
	command line arguments
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument('--f', type=str, default='points.txt',
						help='Enter the filename')
	parser.add_argument('--k', type=int, default=2,
						help='Number of clusters')

	args = parser.parse_args()
	# sys.stdout.write(str(calc(args)))

	data_points = data_read(args.f)
	k_means(data_points ,args.k)

if __name__ == '__main__':
	main()