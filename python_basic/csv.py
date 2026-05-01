##Theory 
import csv
import os

# Assuming you are in your working directory
with open('dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    
    # We can loop through this reader object just like a text file
    for line in csv_reader:
        print(line)
        # Output: ['Alice', '28', 'Engineer']
        
        # If I only wanted their names (Index 0):
        # print(line[0])

##advance method

import csv

with open('dataset.csv', 'r') as f:
    # Use DictReader instead of standard reader
    csv_reader = csv.DictReader(f)
    
    for line in csv_reader:
        # Now we can ask for data by its actual column name!
        print(line['Name'], "is a", line['Profession'])


## writing the csv files

import csv

# We use "w" mode to write. 
# (Note: adding newline='' prevents blank lines between rows on Windows)
with open('new_file.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    
    # Writing a single row (usually used for headers)
    csv_writer.writerow(['Name', 'Status'])
    
    # Writing data rows
    csv_writer.writerow(['System A', 'Active'])
    csv_writer.writerow(['System B', 'Offline'])

TradeID,Ticker,Outcome,Profit_Loss
T-001,AAPL,Win,450.00
T-002,TSLA,Loss,-150.50
T-003,NVDA,Win,890.20
T-004,AMC,Loss,-400.00
T-005,GME,Loss,-50.00
T-006,MSFT,Win,120.00


import csv

with open('raw_trades.csv','r') as f:
    csv_reader=csv.DictReader(f)

    next(csv_reader)
    for line in csv_reader:
        print(line)

        if(line['Outcome']=="Loss"):
            print("It was a loss trade")


with open('postmortem_report.csv','w',newline=" ") as f:
    csv_writer=csv.DictWriter(f)


    csv_writer.writerow(['TradeID','Ticker','Outcome','Profit/Loss'])

    for line in csv_reader:
        if(line['Outcome']=="Loss"):
            print(line)


with open('mq6_logs.csv','r') as file_in,open('critical_alerts.csv','w',newline=' ') as file_out:
    csv_reader=csv.DictReader(file_in)

    header=['Timestamp','Node_ID','Gas_PPM','Connection']

    csv_writer=csv.DictWriter(file_out,fieldnames=header)
    csv_writer.writeheader()

    for line in csv_reader:
        if(line['Gas_PPM']>500):
            csv_writer.writerow(line)





