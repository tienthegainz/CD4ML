class Dataset():
    def __init__(self, config):
        self.config = config

    def __getitem__(self, x):
        pass


def dataset_builder(config):
    return Dataset(config)
