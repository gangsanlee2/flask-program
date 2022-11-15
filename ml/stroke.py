import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
from sklearn.preprocessing import OrdinalEncoder
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split

font_path = "C:/Windows/Fonts/batang.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


STROKE_MENUS = ["종료", #0
                "데이터구하기",#1
                "한글화",#2
                "타깃변수설정",#3
                "ID변수설정",#4
                "구간확률변수설정",#5
                "범주형변수설정",#6
                "결측값이 50% 초과인 변수 제거",#7
                "이상값 제거",#8
                "csv 저장",#9
                "샘플링"]

stroke_meta = {
    'id':'아이디', 'gender':'성별', 'age':'나이', 'hypertension':'고혈압', 'heart_disease':'심장병',
    'ever_married':'기혼여부', 'work_type':'직종', 'Residence_type':'거주형태',
    'avg_glucose_level':'평균혈당', 'bmi':'체질량지수', 'smoking_status':'흡연상태', 'stroke':'뇌졸중'}
stroke_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.target(),
    "4" : lambda t: t.id_variable(),
    "5" : lambda t: t.interval_variable(),
    "6" : lambda t: t.categorical_variable(),
    "7" : lambda t: t.remove_null(),
    "8": lambda t: t.remove_outlier(),
    "9": lambda t: t.additional_process(),
    "10": lambda t: t.sampling()
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''

class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
        self.my_stroke = None
        self.df1 = None
        self.cols = None
        self.cols1 = None
        self.df2 = None
    '''
    1.스펙보기
    '''
    def spec(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))
    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        print(" --- 2.Features ---")
        print(self.my_stroke.columns)
    '''
    3.타깃변수(=종속변수 dependent, y값) 설정
        입력변수(=설명변수, 확률변수, X값)
        타깃변수명 : stroke(=뇌졸중)
        타깃변수값 : 과거에 한 번이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''
    def target(self):
        self.rename_meta()
        df = self.my_stroke
        print(f'stroke type : {df["뇌졸중"].dtype}')
        print(f'stroke null : {df["뇌졸중"].isnull().sum()}')
        print(f'stroke value counts : \n{df["뇌졸중"].value_counts(dropna=False)}')

    def id_variable(self):
        self.target()
        df = self.my_stroke
        print(df['아이디'].dtypes)
        print(f'id 결측값 : {df["아이디"].isnull().sum()}')
        n = len(pd.unique(df['아이디'])) - len(df['아이디'])
        print(f'중복된 id 개수 : {n}')

    def interval_variable(self):
        self.id_variable()
        df = self.my_stroke
        self.cols = ['나이','평균혈당','체질량지수']
        print(df[self.cols].dtypes)
        pd.options.display.float_format = '{:.2f}'.format
        print(df[self.cols].describe())
        c = df['나이'] > 18
        print(f"나이 > 18 : \n{df[c].head(3)}")
        print(f'df[c]의 자료 개수 : {len(df[c])}')
        print(f'df 대비 df[c]의 자료 개수 비율 : {len(df[c])/len(df)}')
        self.df1 = df[c]
        print(f'df1 shape : {self.df1.shape}')

    def categorical_variable(self):
        self.interval_variable()
        df1 = self.df1
        self.cols1 = ['성별','고혈압','심장병','기혼여부','직종','거주형태','흡연상태']
        print(f'cols1 null 개수 : \n{df1[self.cols1].isnull().sum()}')
        print(f'cols1 type : \n{df1[self.cols1].dtypes}')

    def remove_null(self):
        self.interval_variable()
        df1 = self.df1
        df = self.my_stroke
        cols = self.cols
        print(df1.isna().any()[lambda x:x])
        print(f'rate : {df["체질량지수"].isnull().mean()}')
        print(f"외도 : \n{df1[cols].skew()}")
        print(f"첨도 : \n{df1[cols].kurtosis()}")
        print(f"work type : \n{df1['직종'].value_counts(dropna=False)}")
        print(pd.crosstab(df1['직종'],columns='count'))
        print(pd.crosstab(df1['직종'],columns='ratio',normalize=True))
        print(pd.crosstab(df1['직종'],df1['뇌졸중']))
        print(pd.crosstab(df1['직종'],df1['뇌졸중'], normalize=True))

    def remove_outlier(self):
        self.remove_null()
        df1 = self.df1
        df = self.my_stroke
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        sns.histplot(ax=axes[0], data=df, x="나이", kde=True, bins=20)
        sns.histplot(ax=axes[1], data=df, x="평균혈당", kde=True, bins=20)
        sns.histplot(ax=axes[2], data=df, x="체질량지수", kde=True, bins=20)
        plt.show()
        sns.set_style('whitegrid')
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        sns.boxplot(ax=axes[0], x='나이', data=df1)
        sns.boxplot(ax=axes[1], x='평균혈당', data=df1)
        sns.boxplot(ax=axes[2], x='체질량지수', data=df1)
        plt.show()
        Q1 = df1[['나이', '평균혈당', '체질량지수']].quantile(0.25)
        Q3 = df1[['나이', '평균혈당', '체질량지수']].quantile(0.75)
        IQR = Q3 - Q1
        print(f'IQR : \n{IQR}')
        print("*" * 50)
        Lower = Q1 - 3.0 * IQR
        Upper = Q3 + 3.0 * IQR
        print(f'Lower : \n{Lower}')
        print(f'Upper : \n{Upper}')
        print("*" * 50)
        c1 = df1['평균혈당'] <= 232.64
        c2 = df1['체질량지수'] <= 60.3
        self.df2 = df1[c1 & c2]
        print(f'shape : {self.df2.shape}')
        print(self.df2.info())
    def additional_process(self):
        df2 = self.df2
        df2['성별'] = OrdinalEncoder().fit_transform(df2['성별'].values.reshape(-1, 1))
        df2['기혼여부'] = OrdinalEncoder().fit_transform(df2['기혼여부'].values.reshape(-1, 1))
        df2['직종'] = OrdinalEncoder().fit_transform(df2['직종'].values.reshape(-1, 1))
        df2['거주형태'] = OrdinalEncoder().fit_transform(df2['거주형태'].values.reshape(-1, 1))
        df2['흡연여부'] = OrdinalEncoder().fit_transform(df2['흡연여부'].values.reshape(-1, 1))
        '''
        self.df2 = df2
        #self.spec()
        print(" ### 프리프로세스 종료 ### ")
        self.stroke.to_csv("./save/stroke.csv")
        '''
    def sampling(self):
        df = pd.read_csv("./save/stroke.csv")
        data = df.drop(['뇌졸중'], axis=1)
        target = df['뇌졸중']
        undersample = RandomUnderSampler(sampling_strategy=0.333, random_state=2)
        data_under, target_under = undersample.fit_resample(data, target)
        print(target_under.value_counts(dropna=True))
        X_train, X_test, y_train, y_test = train_test_split(data_under, target_under,
                                                            test_size=0.5, random_state=42, stratify=target_under)
        print("X_train shape :", X_train.shape)
        print("X_test shape :", X_test.shape)
        print("y_train shape :", y_train.shape)
        print("y_test shape :", y_test.shape)
        print("y_train value ratio :\n", y_train.value_counts(normalize=True))
        print("y_train value count :\n", y_train.value_counts())
