
import pandas as pd
import module1, module2

class AA(pd.DataFrame):

    def __init__(self):

        super().__init__()

        df_aa = module1.KWDATA()
        df_aa2 = module2.CSVA()

        df_aa = df_aa[['score', 'Phrase', 'Search Volume', df_aa2.master_keyword]]

        df_aa = df_aa[df_aa[df_aa.columns[3]] < 11]
        df_aa = df_aa.reset_index(drop = True)

        df_aa['score'] = df_aa['score'].apply(lambda x: 'AA')
        
        df_aa_dict = df_aa.to_dict()
        self.append(super().__init__(df_aa_dict))