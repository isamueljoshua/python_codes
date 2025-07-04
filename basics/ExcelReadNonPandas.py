"""
Here we use the xlrd library to open a workbook without using pandas

Could be used when you don't know the sheet names of excel files
"""
from xlrd import open_workbook

# Now .xls files only are supported in the xlrd libary
book = open_workbook('ExcelTest.xlsx')
sheet = book.sheet_by_index(0)

# read header values into the list    
keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

dict_list = []
for row_index in xrange(1, sheet.nrows):
    d = {keys[col_index]: sheet.cell(row_index, col_index).value 
         for col_index in xrange(sheet.ncols)}
    dict_list.append(d)

print (dict_list)