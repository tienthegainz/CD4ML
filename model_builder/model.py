import random

param_choices = list(range(0, 20))


class DummyModel2():
    def __init__(self, config):
        self.config = config
        self.params = {
            "layer1": random.sample(param_choices, 5),
            "layer2": random.sample(param_choices, 5),
            "layer3": random.sample(param_choices, 5)
        }
        print('Dummy 1 with params: ', self.params)

    def load_params(self, params):
        print('Loading Dummy1 with params: \n {}'.format(params))
        self.params = params


def model_builder(config, retrain=False, path=None):
    return DummyModel2(config)
