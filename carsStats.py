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

all_data = read_car_data(FILE_PATH)
print(all_data)


[{'Jan 2019': 'Ford Motor Company', 'Feb 2019': '16,629', 'Mar 2019': '10,390', 'Apr 2019': '40,755', 'May 2019': '18,074', 'Jun 2019': '19,892', 'Jul 2019': '22,049', 'Aug 2019': '17,049', 
  None: ['10,764']}, {'Jan 2019': 'Volkswagen UK', 'Feb 2019': '13,224', 'Mar 2019': '7,960', 'Apr 2019': '38,335', 'May 2019': '15,161', 'Jun 2019': '15,737', 'Jul 2019': '20,474', 'Aug 2019': '15,183', 
                      None: ['11,334']}, {'Jan 2019': 'Mercedes-Benz UK', 'Feb 2019': '12,242,29', 'Mar 2019': '6,088', 'Apr 2019': '33,536', 'May 2019': '11,739', 'Jun 2019': '14,431', 'Jul 2019': '14,947', 'Aug 2019': '12,056', None: ['5,040']}, {'Jan 2019': 'Vauxhall Motors', 'Feb 2019': '150', 'Mar 2019': '4,905', 'Apr 2019': '37,769', 'May 2019': '10,639', 'Jun 2019': '13,461', 'Jul 2019': '15,540', 'Aug 2019': '10,398', None: ['4,864']}, {'Jan 2019': 'BMW', 'Feb 2019': '9,553', 'Mar 2019': '6,870', 'Apr 2019': '30,330', 'May 2019': '10,868', 'Jun 2019': '12,415', 'Jul 2019': '19,985', 'Aug 2019': '9,198', None: ['4,853']}]

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