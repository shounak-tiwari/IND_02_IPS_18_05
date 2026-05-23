# Write a program to load excel file and calulate sales profit and  quantity state vise using for loops.... 
import openpyxl
wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\IPS_DATA\Superstore-1.xlsx")

sheet = wb['Orders']
totalsales = 0 
totalprofit = 0 

state = input("Enter the state for check the total sales :  ").title()
for data in sheet.iter_rows(values_only=True):
    if(data[10]==state):
        totalsales = totalsales+data[17]
        totalprofit = totalprofit+data[20]

print(totalsales)
print(totalprofit)