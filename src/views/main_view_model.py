from src import models


class MainViewModel(object):
    def __init__(self):
        self.nutrients: [models.Nutrient] = []
        self.customers: [models.Customer] = []
