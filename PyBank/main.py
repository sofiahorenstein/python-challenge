import os
import csv


print ("Financial Analysis")
print (" ----------------------------------------- ")

budget_data_csv = os.path.join("..", "PyBank", "budget_data.csv")

columnsOfData = []

with open(budget_data_csv) as f:
    columnsOfData = list(csv.reader(f))

dates = []
amounts = []
for x in range(0, len(columnsOfData)):
    dates.append(columnsOfData[x][0])
    amounts.append(columnsOfData[x][1])

# Invoking native Python List POP to remove the 'header' of CSV column ( located at index[0] )
dates.pop(0)
amounts.pop(0)

# Invoking LIST COMPREHENSION to manually cast list of STRINGS into list of FLOATS
amounts = [float(x) for x in amounts]

print("# of Months:", len(dates))
print("Total: $", sum(amounts))

startingAmount = amounts[0]
endingAmount = amounts[-1]
averageChangeWithinPeriod = (startingAmount + endingAmount)/2

percentChanges = []
dollar_differences = []
for x in range(1, len(amounts)):
   initialAmt = amounts[x-1]
   finalAmt = amounts[x]

   difference = (finalAmt - initialAmt)
   dollar_differences.append(difference)

print("Average Dollar Change within Period: $", round(averageChangeWithinPeriod, 2))
print("Greatest INCREASE in Profits: $", max(dollar_differences))
print("Greatest DECREASE in Profits: $", min(dollar_differences))
