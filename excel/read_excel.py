
from xlrd import open_workbook,cellname
book = open_workbook('dts.xlsx')
sheet = book.sheet_by_index(0)
#print sheet.name
#print sheet.nrows
#print sheet.ncols

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        #print cellname(row_index,col_index),'-', type(cellname(row_index,col_index)),
        if sheet.cell(row_index,col_index).value != "":
            if row_index != (sheet.nrows-1):
                print ' ' * 4 * row_index, sheet.cell(row_index,col_index).value
            else:
                print 'Hej ' * 4 * row_index, sheet.cell(row_index,col_index).value,