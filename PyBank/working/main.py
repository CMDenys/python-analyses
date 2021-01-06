#import dependencies
import os 
import csv



#create a path to the data file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')



total_months = []
profit_loss = []
change_pl = []

#create a starting point for row count
total_profits = 0
profit_change = 0
sum_changes = 0


#open and read data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #loop through the rows to get a count. Found solution at https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
    #remove header
    header = next(csvreader)


    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(int(row[1]))



    for i in range(1, len(profit_loss)):
        #store differences in new list
        change_pl.append(profit_loss[i] - profit_loss[i - 1])
        avg_change = sum(change_pl) / len(change_pl)

        greatest_profit = max(change_pl)
        greatest_loss = min(change_pl)

        #need to index into where the greatest profit and loss happened in total months
        max_date = change_pl.index(greatest_profit) + 1
        min_date = change_pl.index(greatest_loss) + 1
        
print('```')
print('Financial Analysis')
print('-------------------------------')
print(f'Total Months: {len(total_months)}')    
print(f'Total Profits: ${sum(profit_loss)}')
print(f'Average Change: ${round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {total_months[max_date]} (${greatest_profit})')
print(f'Greatest Decrease in Profits: {total_months[min_date]} (${greatest_loss})')
print('```')



    
   
    

