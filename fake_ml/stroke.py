import pandas as pd


class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
        self.stroke = None
        self.count_test = None


    def rename_meta(self):
        self.my_stroke = self.mpg.rename(columns=stroke_meta)
        print(" --- 2.Features ---")
        print(self.my_stroke.columns)