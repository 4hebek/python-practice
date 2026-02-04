# read data and display the following
# sum of cars sold in each month for all manufacturers
# total yearly sales by each manufacturer for all years and manufactures

# grant total:

# zip()
# csvReader_

FILE_PATH = "cars.csv"

import csv

def read_data(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    return headers, rows

        
        
    #     data = [row for row in csv_reader]
    return data

all_data = read_data(FILE_PATH)
print(all_data)

# def calculate_monthly_sales(data):
#     monthly_sales = {}
#     for row in data:
#         month = row['Month']
#         sales = int(row['Sales'])
#         if month not in monthly_sales:
#             monthly_sales[month] = 0
#         monthly_sales[month] += sales
#     return monthly_sales

# def calculate_yearly_sales(data):
#     yearly_sales = {}
#     for row in data:
#         manufacturer = row['Manufacturer']
#         sales = int(row['Sales'])
#         if manufacturer not in yearly_sales:
#             yearly_sales[manufacturer] = 0
#         yearly_sales[manufacturer] += sales
#     return yearly_sales 