#import dependencies
import os 
import csv


#create a path to the data file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


month_count = []
profit = []
profit_change = []

#create a starting point for row count
num_rows = 0

#open and read data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #loop through the rows to get a count. Found solution at https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
    #remove header
    header = next(csvreader)
    for row in csvreader:
        num_rows += 1
    
    print(f'Total Months: {num_rows}')