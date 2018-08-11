from .DatasetReader import DatasetReader
import scipy.io as sio

class MatReader(DatasetReader):
    def __init__(self, path, custom_function=None):        
        self.path = path
        self.custom_function = custom_function or (lambda mat: [list(mat['Data'][i]) for i in range(len(mat['Data']))])
    
    def read_dataset(self):
        mat = sio.loadmat(self.path)               
        if 'x' in mat:
            X,Y = map(list, mat['x']), map(list, mat['y'])        
            return [X[i]+Y[i] for i in range(len(X))]
        #if 'X' in mat:
        #    X,Y = map(list, mat['X']), map(list, mat['Y'])        
        #    return [X[i]+Y[i] for i in range(len(X))]        
        if 'Data' in mat:            
            return self.custom_function(mat)     
        if self.custom_function:
            return self.custom_function(mat)
        return []
        