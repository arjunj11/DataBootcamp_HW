import os
import csv
s=i=l=maxi=max=0
a=[]  # list of candidates
b=[] # counting the votes of the canditates
c=[]# for % of the votes for each canditate
j=""
filepath1=os.path.join("PyPoll","Resources","election_data.csv")
with open(filepath1,'r') as file1:
    fileread1=csv.reader(file1,delimiter=',')
    
    next(fileread1, None)  # skip the headers
    for row in fileread1:
        if(row[0]!=i):
            s=s+1
        i=row[0]

        for k in range(0,len(a)):
            if(a[k]==row[2]):     # comparing it to any entry from the list of canditates 
                l=1
        if(l==0):
            a.append(str(row[2]))
        l=0
    for n in range(0,len(a)):
        b.append(0)
        c.append(0)
    file1.seek(0)   # to bring back the cursor on the zeroeth position in the file

    for m in range(0,len(a)):
        for row1 in fileread1:
            if((row1[2])==a[m]):  #counting how many times in the file the name of the canditate appears
                b[m]=b[m]+1
        file1.seek(0)
        c[m]=100*b[m]/s
        if maxi<c[m]:
            maxi=c[m]
            max=m
        
filepath2=os.path.join("PyPoll","Resources","result.txt")
with open (filepath2,'w') as file2:
    file2.write("My analysis is as follows\n\n")
    file2.write("________________________________\n")
    file2.write(f"Total votes caste were {s}\n")
    file2.write("________________________________\n")
    for o in range(0,len(a)):
        file2.write(f"{a[o]} got {b[o]} votes making his  percentage to {round(c[o],3)}\n")
    file2.write(f"And the WINNER izzzzz {a[max]} with vote percentage of {round(maxi,3)}")

with open(filepath2,'r') as file2:
    fileread2=csv.reader(file2,delimiter=',')
    for row2 in fileread2:
        print(row2)

            
