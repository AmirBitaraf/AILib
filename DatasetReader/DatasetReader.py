class DatasetReader(object):
    """DatasetReader Abstract Class"""
    def __init__(self, path, custom_function=None):
        raise NotImplementedError

    def read_dataset(self):
        """Reads the dataset in following format"""
        raise NotImplementedError
