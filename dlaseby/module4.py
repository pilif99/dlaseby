
import pandas as pd
import module2, module3

class MKW(pd.DataFrame):

    def __init__(self):

        super().__init__()

        df_mkw1 = module2.CSVA()
        df_mkw1 = df_mkw1[['score', 'Phrase', 'Search Volume', df_mkw1.master_keyword]]
        df_mkw2 = module3.AA()

        df_mkw = pd.concat([df_mkw1, df_mkw2])
        df_mkw = df_mkw.drop_duplicates(subset = 'Phrase')
        
        df_mkw = df_mkw.sort_values(by = [df_mkw.columns[2]], ascending=False)
        df_mkw = df_mkw.reset_index(drop = True)


        pd.set_option("display.max_rows", None, "display.max_columns", None)
        
        df_mkw_dict = df_mkw.to_dict()
        self.append(super().__init__(df_mkw_dict))