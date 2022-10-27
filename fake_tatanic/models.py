from util.dataset import Dataset
import pandas as pd

class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        model = self.new_model(fname=self.dataset.fname)
        return f'Train type: {type(model)}\n' \
               '''
               f'Train columns: {model.columns}\n' \
               f'Train head: {model.head(n=10)}\n' \
               f'Train tail: {model.tail(n=10)}\n' \
               f'Train null의 개수: {model.isnull().sum()}'
               '''

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) -> object:
        return this.train["Survived"]

    @staticmethod
    def drop_features(this, *feature) -> object:
        for i in feature
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this