import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
output = os.path.join('PyBank','analysis','Results.txt')
# initialize counters
months = 0
net = 0
changes = []
lastchng = 0
bigprofit = 0
bpdate = ""
bigloss = 0
bldate = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#begin reading and evaluating each row
    for row in csvreader:
        #step up the variables
        months += 1
        value = int(row[1])
        net += value

        #avoids accidentally calculating the header row
        if lastchng != 0:
            change = value-lastchng
            changes.append(change) #Adding the net change to a list
            lastchng = value
            if change > bigprofit: #Logic for finding greatest increase/decrease in profits
                bigprofit = change
                bpdate = row[0]
            if change < bigloss:
                bigloss = change
                bldate = row[0]
        lastchng = value

    avgchange = sum(changes)/len(changes) #Calculating average change using list

    #Outputting results to text file and terminal
    outputtext = f"Financial Analyisis \n----------------------- \nTotal Months: {months} \nTotal : ${net} \nAverage Change: ${avgchange} \nGreatest Increase in Profits: {bpdate} (${bigprofit}) \nGreatest Decrease in Profits: {bldate} (${bigloss})"
    print(outputtext)
    with open(output,"w") as file:
        print(outputtext, file=file)