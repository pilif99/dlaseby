
import pandas as pd
import module1

class CSVA(pd.DataFrame):

    def __init__(self):

        def masterKeyword():
            
            asiny = {}
            for i in range(len(df_csva.columns) - 3):
                asiny[df_csva[df_csva[df_csva.columns[i + 3]] < 11].sum()['Search Volume']] = df_csva.columns[i+3]
            a = []
            for i in asiny:
                a.append(i)
            return asiny[max(a)]

        super().__init__()

        df_csva = module1.KWDATA()
        df_csva = df_csva[df_csva.score > 2]

        self.master_keyword = masterKeyword()
        
        df_csva_dict = df_csva.to_dict()
        self.append(super().__init__(df_csva_dict))