import csv
import numpy as np

DIMENSION = 2
COUNT = 50

with open('sample.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for _ in range(COUNT):
        writer.writerow([np.random.randint(0, 100) for i in range(DIMENSION)])