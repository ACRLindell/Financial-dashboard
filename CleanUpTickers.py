import csv

with open("./Stockdata/Tickers.txt",'r') as temp:
    contents = temp.readlines()
    #print(contents[2])
csvfile ="/Users/alexanderlindell/Documents/Programmering /Python/Stock dashboard/Tickers.csv"
headers={'Company','Ticker'}
try: 
    with open(csvfile,'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=headers)
        writer.writeheader()
        for row in contents: 
            temp = row.split('STO:',1)
            temp[0]=temp[0].replace("\t","")
            temp[1]=temp[1].replace("\n","")
            temp[1]=temp[1] + '.ST'
            print(temp)
            writer.writerow({'Company': temp[0],'Ticker': temp[1]})
except IOError:
    print("I/O Error")
