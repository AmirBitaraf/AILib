from DatasetReader.CSVReader import CSVReader
from DatasetReader.DatasetReader import DatasetReader
import numpy as np
import random

class Dataset(object):
    def __init__(self, path=None, frmt=CSVReader, data=[], name=None, custom_function=None):
        if path:
            datareader = frmt(path, custom_function)
            self._data = datareader.read_dataset()
        else:
            self._data = data
        self.name = name or path

    def length(self):
        return len(self._data)    

    def data(self):
        return self._data

    def npdata(self):
        return np.array(self._data)

    def split(self, percentage=0.70):
        data = self._data[:]
        chosen = [data.pop(random.randrange(len(data))) for _ in range(int(len(self._data)*percentage))]
        return Dataset(data=chosen), Dataset(data=data)

    def copy(self):
        data = self._data[:]        
        return Dataset(data=data)

    def features(self):
        return [x[:-1] for x in self._data]

    def add_noise(self, noise=0.05):
        data = [x[:-1] for x in self._data]
        min_max = [
            [min([data[i][j] for i in range(len(data))]), max([data[i][j] for i in range(len(data))])]
            for j in range(len(data[0]))
        ]
        for i in random.sample(range(len(data)),int(noise*len(data))):
            for j in range(len(data[0])):
                self._data[i][j] = (min_max[j][1]-min_max[j][0])*(np.random.normal()/2.0)+min_max[j][0]

    def sp_noise(self, prob=0.30):
        output = self._data[:]
        for i in range(len(output)):
            noises = random.sample(range(len(output[i])), int(len(output[i])*prob))
            for j in noises:
                rdn = random.random()
                if rdn < 0.5:
                    output[i][j] = 0
                else:
                    output[i][j] = 255
        return Dataset(data=output)

    def normalized_features(self):
        data = [x[:-1] for x in self._data]
        norm_array = [
            np.linalg.norm([data[i][j] for i in range(len(data))])
            for j in range(len(data[0]))
        ]
        data = [
            [data[i][j]/norm_array[j] for j in range(len(data[i]))]
            for i in range(len(data))
        ]
        return data                
    
    def classes(self, class_type=str):
        return [class_type(x[-1]) for x in self._data]
    
    def classes_int(self):
        return [int(x[-1]) for x in self._data]    

    def features_count(self):
        return len(self._data[0])-1

    def values(self, column):
        return set(map(lambda x: x[column], self._data))

    def column(self, column):
        return np.array(map(lambda x: x[column], self._data))

    def filter(self, column, value):
        filtered = filter(lambda x: x[column]==value, self._data)
        return Dataset(data=map(lambda x: x[:column]+x[column+1:], filtered))

    def binarize(self):
        cl = set(self.classes())
        if len(cl) > 2:
            raise Exception("Cannot binarize data with more than two classes!")
        mp = {}
        mp[str(cl.pop())] = -1
        mp[str(cl.pop())] = 1
        data = self._data[:]
        data = [row[:-1]+[mp[str(row[-1])]] for row in data]
        return Dataset(data=data)