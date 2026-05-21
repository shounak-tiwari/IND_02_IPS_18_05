import openpyxl
workbook = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\02_IPS\20_05_2026\databook.xlsx")

sheet = workbook.active

add = 0 
count = 0 
for row in sheet.iter_rows(min_row=2,values_only=True):
    print(row[0])
    add = add +row[0]
    count+=1

print("sum of all observation : ",add)
print("number of all observation : ",count)

print("mean =  ",add/count)

