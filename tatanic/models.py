'''
인스턴스 생성시

내부에 있는 클래스를 가져와 쓸 때 → new_~

외부에 있는 파일을 가져와 쓸 때 → create_~
'''


import numpy as np
import pandas as pd
import seaborn as sns
from util.dataset import Dataset
'''
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
                    'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
시각화를 통해 얻은 상관관계 변수(variable = feature = column)는
Pclass
Sex
Age
Fare
Embarked
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

    def new_model(self, fname) -> object: # 프로토타입
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df

    @staticmethod
    def create_train(this) -> object: #여기서 object는 df를 의미
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) -> object:   # create_test 대신 create_label로 주로 쓰인다.
        return this.train["Survived"]

    @staticmethod
    def drop_features(this, *feature) -> object:     # *feature 는 자료구조 []
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        train = this.train
        test = this.test
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        '''
        ls = []
        ls.append(this.train)
        ls.append(this.test)
        -> not pythonic ->
        ls = [this.train, this.test]
        for i in ls:
        ->
        for i in [this.train, this.test]:
        '''
        '''
        gender_mapping = {"male" : 0, "female" : 1}
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map(gender_mapping)
        ->
        '''
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male": 0, "female": 1})
        return this

    @staticmethod
    def age_ordinal(this) -> object: # 연령대 10대, 20대, 30대
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)
        bins = [-1,0,5,12,18,24,34,68,np.inf] # bin : 통, 계급   inf : infinite
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this


    @staticmethod
    def fare_ordinal(this) -> object:
        train = this.train
        test = this.test
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels={1,2,3,4})
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'}) # NaN : Not a Number
        this.test = this.test.fillna({'Embarked': 'S'})
        for i in [this.train, this.test]:
            #i['Departure'] = i['Embarked'].map({"S": 1, "C": 2, "Q": 3})
            i['Embarked'] = i['Embarked'].map({"S":1, "C":2, "Q":3})
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for i in combine:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            i['Title'] = i['Title'].replace('mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map({
                'Mr': 1,
                'Miss': 2,
                'Mrs': 3,
                'Master': 4,
                'Royal': 5,
                'Rare': 6
            })
        return this


if __name__ == '__main__':   # 나중에 지워야 함. 단지 디버깅 목적
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    '''
    this = TitanicModel.sex_nominal(this)
    print(this.train['Gender'])
    print(this.test['Gender'])
    print(this.train.columns)
    print(this.train.head(n=10)
    '''
    '''
    this = TitanicModel.fare_ordinal(this)
    print(this.train['FareBand'])
    print(this.train['FareBand'].value_counts())
    '''
    '''
    this = TitanicModel.age_ordinal(this)
    print(this.train.columns)
    print(f"null의 개수 :{this.train['Age'].isnull().sum()}")
    print(this.train.head(n=10))
    '''
    this = t.embarked_nominal(this)
    print(this.train.columns)  # columns는 메소드가 X. 그래서 columns() X
    print(this.train.head(n=10))