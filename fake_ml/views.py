import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class StrokeController:

    @staticmethod
    def set_data(this):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        df = pd.read_csv('./data/'+this)

        print(df.head(3))
        print("*"*50)
        print(df.shape)
        print("*" * 50)
        print(df.info())
        print("*" * 50)
        print(df['id'].dtypes)
        print("*" * 50)
        print(f'id 결측값 : {df["id"].isnull().sum()}')
        n = len(pd.unique(df['id'])) - len(df['id'])
        print(f'중복된 id 개수 : {n}')
        print("*" * 50)
        print(f'stroke type : {df["stroke"].dtype}')
        print(f'stroke null : {df["stroke"].isnull().sum()}')
        print(f'stroke value counts : \n{df["stroke"].value_counts(dropna=False)}')
        print("*" * 50)
        cols = ['age','avg_glucose_level','bmi']
        print(df[cols].dtypes)
        print("*" * 50)
        pd.options.display.float_format = '{:.2f}'.format
        print(df[cols].describe())
        print("*" * 50)
        c = df['age'] > 18
        print(f"age > 18 : \n{df[c].head(3)}")
        print(f'df[c]의 자료 개수 : {len(df[c])}')
        print(f'df 대비 df[c]의 자료 개수 비율 : {len(df[c])/len(df)}')
        print("*" * 50)
        df1 = df[c]
        print(f'df1 shape : {df1.shape}')
        df1 = df1.rename(columns={'Residence_type' : 'residence_type'})
        cols1 = ['gender','hypertension','heart_disease','ever_married','work_type','residence_type','smoking_status']
        print(f'cols1 null 개수 : \n{df1[cols1].isnull().sum()}')
        print("*" * 50)
        print(f'cols1 type : \n{df1[cols1].dtypes}')
        print("*" * 50)
        print(df1.isna().any()[lambda x:x])
        print(f'rate : {df["bmi"].isnull().mean()}')
        print("*" * 50)
        print(f"외도 : \n{df1[cols].skew()}")
        print("*" * 50)
        print(f"첨도 : \n{df1[cols].kurtosis()}")
        print("*" * 50)
        print(f"work type : \n{df1['work_type'].value_counts(dropna=False)}")
        print("*" * 50)
        print(pd.crosstab(df1['work_type'],columns='count'))
        print("*" * 50)
        print(pd.crosstab(df1['work_type'],columns='ratio',normalize=True))
        print("*" * 50)
        print(pd.crosstab(df1['work_type'],df1['stroke']))
        print("*" * 50)
        print(pd.crosstab(df1['work_type'],df1['stroke'], normalize=True))
        print("*" * 50)
        fig, axes = plt.subplots(1,3,figsize=(15,4))

        sns.histplot(ax=axes[0], data=df, x="age", kde=True, bins=20)
        sns.histplot(ax=axes[1], data=df, x="avg_glucose_level", kde=True, bins=20)
        sns.histplot(ax=axes[2], data=df, x="bmi", kde=True, bins=20)
        plt.show()

        sns.set_style('whitegrid')

        fig, axes = plt.subplots(1,3,figsize=(15,4))

        sns.boxplot(ax=axes[0], x='age', data=df1)
        sns.boxplot(ax=axes[1], x='avg_glucose_level', data=df1)
        sns.boxplot(ax=axes[2], x='bmi', data=df1)
        plt.show()
        Q1 = df1[['age','avg_glucose_level','bmi']].quantile(0.25)
        Q3 = df1[['age','avg_glucose_level','bmi']].quantile(0.75)
        IQR = Q3 - Q1
        print(IQR)
        print("*" * 50)
        Lower = Q1-3.0*IQR
        Upper = Q3+3.0*IQR
        print(f'Lower : \n{Lower}')
        print(f'Upper : \n{Upper}')
        print("*" * 50)
        c1 = df1['avg_glucose_level'] <= 232.64
        c2 = df1['bmi'] <= 60.3
        df2 = df1[c1 & c2]
        print(f'shape : {df2.shape}')
        print("*" * 50)
        cols = ['age','avg_glucose_level','bmi']
        print(round(df2[cols].corr(),2))
        corr = df2[cols].corr()
        annot_kws = {"ha": 'center', "va": 'top'}
        sns.heatmap(data=corr, annot=True, annot_kws=annot_kws, cmap="YlGnBu")
        plt.show()
        df2.to_csv('./data/healthcare-dataset-stroke-data-2.csv', index=False)

if __name__ == "__main__":
    df = pd.read_csv('./data/healthcare-dataset-stroke-data-2.csv')
    print(df.shape)
    print("*" * 50)
    sns.histplot(data=df, x='age', hue='stroke', bins=20)
    plt.show()

    sns.set_style('whitegrid')
    sns.boxplot(x='stroke',y='age',data=df)
    plt.show()

    group = df['age'].groupby(df['stroke'])
    print(group.mean())
    print("*" * 50)
    fig, axes = plt.subplots(1,2,figsize=(15,4))
    sns.histplot(ax=axes[0],data=df,x="avg_glucose_level",hue="stroke",bins=20)
    sns.histplot(ax=axes[1],data=df,x="bmi",hue='stroke',bins=20)
    plt.show()