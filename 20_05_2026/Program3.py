# WAP for calculate total expensens company after deduct 4.8% pf  salary is load from excel salary columns 
import openpyxl
wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\02_IPS\20_05_2026\salary.xlsx")
sheet = wb.active
total = 0 
for row in sheet.iter_rows(values_only=True,min_row=2):
    salary = row[1] - ((row[1]*4.8)/100)
    total +=salary

print(round(total))