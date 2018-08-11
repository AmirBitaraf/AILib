from .DatasetReader import DatasetReader

class SplitReader(DatasetReader):
    def __init__(self, path, custom_function=None):        
        self.path = path
    
    def read_dataset(self):
        ret = []
        for line in  open(self.path, 'r'):            
            ret.append(map(float, line.split()))                
        return ret