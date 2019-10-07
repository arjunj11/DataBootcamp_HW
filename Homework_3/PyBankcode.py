import os
import csv
tm=s=maxi=mini=averagechange=net_profitloss=j=0
i=tmin=tmax="yes"
change=[]
filepath1=os.path.join("PyBank","Resources","budget_data.csv")
with open(filepath1,'r') as file1:
    fileread1=csv.DictReader(file1,delimiter=',') #here fileread1 is an object
    for row in fileread1:
        if(row["Date"]!=i):
            tm=tm+1
        i=row["Date"]
        net_profitloss=net_profitloss+float(row["Profit/Losses"]) #gives the netprofitloss
        change.append(float(row["Profit/Losses"])-j)
        if(maxi<(float(row["Profit/Losses"])-j)):
            maxi=float(row["Profit/Losses"])-j
            tmax=row["Date"]
        if(mini>(float(row["Profit/Losses"])-j)):
            mini=float(row["Profit/Losses"])-j
            tmin=row["Date"]
        j=float(row["Profit/Losses"])
        
#average change in Profit/Losses
    for k in range(1,len(change)):
        s+=change[k]
    averagechange=s/(len(change)-1)   # length minus one because i want to remove the first row from the account
    

newfile="result.txt"
filepath2=os.path.join("PyBank","Resources",newfile)
with open(filepath2,'w') as file2:
    file2.write("My analysis is as follows\n")
    file2.write(f"Total number of months included in the dataset are {tm}\n")
    file2.write(f"The net total amount of profit/losses is  {net_profitloss}\n")
    file2.write(f"The average change of the profit/losses is {averagechange}\n")
    file2.write(f"The greatest increase in profits is {maxi} on {tmax}\n")
    file2.write(f"The greatest decrease in losses is {mini} on {tmin}\n")
with open(filepath2,'r') as file2:
    fileread2=csv.reader(file2,delimiter=',')
    for row2 in fileread2:
        print(row2)