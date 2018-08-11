from .DatasetReader import DatasetReader
import csv

class CSVReader(DatasetReader):
    def __init__(self, path, custom_function=None):        
        self.path = path
    
    def read_dataset(self):
        ret = []
        with open(self.path, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                ret.append(map(float, row))
        return ret
