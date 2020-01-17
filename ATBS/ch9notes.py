#openpyxl notes 

#openpyxl.load_workbook(): Works like the open() function in regular python. Put the
   # filename you want to open in parantheses. 
    wb = openpyxl.load_workbook('5/3/1.xlxs')

#openpyxl.get_sheet_names(): Gets the names of all the spreadsheets in the
    #active workbook.

    wb.get_sheet_names()
    #xl shows 'sheets 1, 2, 3' by default. 
    ['Sheet1', 'Sheet2', 'Sheet3',]

#get_sheet_by_names : takes a specific sheet from the workbook and gives it
    # to a variable. Give it the name of the sheet you want in parantheses.
    sheet = wb.get_sheet_by_names('Sheet1')

#openpyxl.value: Shows the contents (value) of a spreadsheet cell. It can 
    #also be used to input new values. 

    sheet['C1'].value 
    73
    sheet['C1'].value = 42

#openpyxl.save: Saves any changes made to your spreadsheet. 
    wb.save('example1.xlsx')

#.title: shows the title of a sheet, or changes the name. 
    sheet.title
    'Sheet1'
    sheet.title = 'New sheet name'

#.cell(row = , column = ) another way to call a specific cell in the sheet.
    # useful if you want to use numbers in a loop instead of string cell names.
    sheet['C1'].value
    42
    sheet.cell(row=1, column=3).value
    42

#.create_sheet(title = , index =optional): Creates a new sheet in your workbook.
    #optional index paramater tells it where to put it in the wb, defaulting
    #at the end. 

    wb.create_sheet(title= 'My New Sheet', index= 0)