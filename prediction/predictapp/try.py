import openpyxl

wb = openpyxl.load_workbook(r"C:\Web Programming\hack\prediction\Book1.xlsx")

sh = wb['Sheet1']
print(sh['A4'].value)

sh['B4'].value = 'Harsh'