import pandas as pd

from util.dataset import Dataset
'''
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
                    'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
             === null 값 ===
            Age            177
            Cabin          687
            Embarked         2
'''

class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        mtx = self.new_model(fname=self.dataset.fname)
        return f'Train type: {type(mtx)}\n' \
               f'Train columns: {mtx.columns}\n' \
               f'Train head: {mtx.head}\n' \
               f'Train null의 개수: {mtx.isnull().sum()}'

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df

    @staticmethod
    def create_train(this) -> object: #여기서 object는 df를 의미
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) -> object:
        return this.train["Survived"]

    @staticmethod
    def drop_features(this, *feature) -> object:     # *feature 는 자료구조 []
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    if __name__ == '__main__': # 나중에 지워야 함. 단지 디버깅 목적
        t= TitanicModel()
        print(t)