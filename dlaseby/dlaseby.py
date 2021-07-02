
from openpyxl import Workbook
import module4
class Glowna:
    
    def __init__(self):

        df = module4.MKW()
        wb = Workbook()
        wb.save('keywordy.xlsx')
        df.to_excel('keywordy.xlsx', index = False)

a = Glowna()