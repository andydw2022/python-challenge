import os
import csv

#locate the source data file
budgetdata = os.path.join("Resources", 'budget_data.csv')

#Variables to store totals
GtLoss=0
GtLoss_Mth=""
GtProfit=0
GtTotal= 0
GtProfit_Mth=""
month=0
AvgChange=0

# Use encoding for Windows
with open(budgetdata, newline='', encoding='utf-8') as csvfile:
    #
    #Loop through every row of data skipping the first line which is the header. save it 
    #
    header= next (csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #Count the months as we go along
        month=month+1
        #Keep a running total from each month
        GtTotal= GtTotal + int(row[1])
        #Keep track of Greatest and Lowest profits/lossess
        if float(row[1]) > 0:
            if float(row[1]) > GtProfit:
               GtProfit = int(row[1])
               GtProfit_Mth = row[0]
        else:
            if int(row[1]) < GtLoss:
                GtLoss = int(row[1])
                GtLoss_Mth = row[0]
    #
    #Calculate average earnings over all the months
    #
    AvgChange = round(GtTotal/month,2)
    
    #output the  results to he screen
    print ("  Financial Analysis")
    print ("---------------------------------------------------------------------")
    print ("")
    print ("Total Months: " + str(month))    
    print ("Total: $" +  str(GtTotal))
    print ("Average  Change: $" + str(AvgChange))
    print ("Greatest Increase in Profits: " + GtProfit_Mth + " $(" + str(GtProfit) +")")
    print ("Greatest Decrease in Profits: " + GtLoss_Mth + " $(" + str(GtLoss)+")")
    print ("---------------------------------------------------------------------")  

# Set variable for output file
output_file = os.path.join("analysis","FinancialAnalysisResults.txt")

#  Open the output file and write the same results to a file
newline="\n"
with open(output_file, "w") as datafile:
    # Write the header row
    (datafile)
    datafile.write("Financial Analysis"+newline)
    datafile.write("---------------------------------------------------------------------"+newline)
    datafile.write(newline)
    datafile.write ("Total Months: " + str(month) +newline)
    datafile.write ("Total: $" +  str(GtTotal)+newline)
    datafile.write ("Average  Change: $" + str(AvgChange)+newline)
    datafile.write ("Greatest Increase in Profits: " + GtProfit_Mth + " $(" + str(GtProfit) +")"+newline)
    datafile.write ("Greatest Decrease in Profits: " + GtLoss_Mth + " $(" + str(GtLoss)+")"+newline)
    datafile.write ("---------------------------------------------------------------------"+newline)  
