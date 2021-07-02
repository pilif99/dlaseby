
import pandas as pd

class KWDATA(pd.DataFrame):

    def __init__(self):

        super().__init__()
        df_kwdata = pd.read_excel('excel.xlsx')
        df_kwdata = df_kwdata.replace('>306', 306)
        df_kwdata = df_kwdata.replace('N/R', 306)
        df_kwdata = df_kwdata.replace('-', 306)
        
        df_kwdata2 = df_kwdata.drop(columns = ['Phrase'])

        df_kwdata= df_kwdata.assign(score = df_kwdata2[df_kwdata2 < 31].count(axis = 1))

        kolumny = df_kwdata.columns.tolist()
        kolumny = kolumny[-1:] + kolumny[:-1]
        df_kwdata = df_kwdata[kolumny]
        df_kwdata_dict = df_kwdata.to_dict()
        self.append(super().__init__(df_kwdata_dict))