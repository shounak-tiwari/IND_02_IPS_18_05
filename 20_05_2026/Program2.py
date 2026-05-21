import openpyxl

wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\02_IPS\20_05_2026\sales data.xlsx")

sheet = wb.active

total = 0

for row in sheet.iter_rows(min_row=2, max_row=10,values_only=True):
    total = total + row[2]

print(total)