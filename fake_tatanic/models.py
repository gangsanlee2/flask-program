from util.dataset import Dataset
import pandas as pd
import numpy as np

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
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male":0, "female":1})
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)
        bins = [-1,0,5,12,18,24,34,68,np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        for i in [this.train, this.test]:
            labels = {1,2,3,4}
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels=labels)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:

        for i in [this.train, this.test]:
            i = i.fillna({'Embarked':'S'})
        '''
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        '''
        for i in [this.train, this.test]:
            i['Departure'] = i['Embarked'].map({"S":1, "C":2, "Q":3})
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-za-z]+)\.', expand=False)
        for j in combine:
            j['Title'] = j['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            j['Title'] = j['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            j['Title'] = j['Title'].replace('mlle', 'Mr')
            j['Title'] = j['Title'].replace('Ms', 'Miss')
            j['Title'] = j['Title'].fillna(0)
            j['Title'] = j['Title'].map({'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6})
        return this

if __name__ == '__main__':
    model = TitanicModel()
    this = Dataset()
    this.train = model.new_model('train.csv')
    this.test = model.new_model('test.csv')
    this = model.embarked_nominal(this)
    print(this.train)