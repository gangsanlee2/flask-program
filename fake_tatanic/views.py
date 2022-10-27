from fake_tatanic import TitanicModel
from util.dataset import Dataset


class TitanicController(object):
    model = TitanicModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()

    def preprocess(self, train, test) -> object:
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']

        return this

    def modeling(self, train, test) -> object:
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self):
        pass

    def submit(self):
        pass