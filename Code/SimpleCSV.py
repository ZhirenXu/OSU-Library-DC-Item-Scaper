import csv
import sys

##open csv file and read handler link, store in a list
# @param    csvName
#           the file name user typed in
# @return   urlList
#           a list contain item url that need to be scraped
def readCSV(csvName):
    urlList = []

    try:
        inFile = open(csvName, 'r')
        csvReader = csv.reader(inFile, delimiter=',')
        for row in csvReader:
            urlList.append(row[0])
        # del the column name read for first line
        urlList.pop(0)
        print ("Open input CSV success.")
    except:
        print("Fail to open input CSV. Press enter to exit.")
        key = input()
        sys.exit()
        
    return urlList

##write category and data into csv file
# @param    dataList
#           a list contains data
# @param    outputFile
#           output File pointed by user, unopened
def writeCSV(dataList, outputFile):
    try:
        csvWriter = csv.writer(outputFile)
        csvWriter.writerow(dataList)
        #print("Write into CSV success.")
    except:
        print("Fail to write into CSV!")

##get input CSV file name
# @return       fileIn
#               Input CSV file
def getCSVInput():
    print("Please enter csv file name with .csv. \nThe file must in the same folder with your main.py program: ")
    fileIn = input()

    return fileIn

##get output CSV file name
# @return       fileOut
#               Output CSV file
def getCSVOutput():
    print("Please enter output file name (with .csv): ")
    fileOut = input()
 
    return fileOut

## read specific column/columns into to list
# @param    csvName
#           input csv file name
# @param    *columnNum
#           An arg, when there is mutiple value it is allowed to store
#           multiple columns in lists
# @return   finalResult
#           A list contain lists of selected column
def readColomn(csvName, *columnNum):
    urlList = []
    #interim = []
    colomn = []
    finalResult = []
    i = 1;
    
    try:
        inFile = open(csvName, 'r')
        csvReader = csv.reader(inFile, delimiter=',')
        try:
            for row in csvReader:
               finalResult.append(row[0])
            # pop hearder
            finalResult.pop(0)
            # pop 'id' header (not activated)
            #interim.pop(0)
            #for num in columnNum:
                #for row in interim:
                    #colomn.append(row[num])
                #finalResult.append(colomn)
                #colomn = []
        except:
            print("Error in reading data. Please notice programmer if you see this error\n")
            print("Press any key to exit")
            input()
            sys.exit()
    except:
        print("\nfail to open csv file.")
        print("Press any key to exit")
        input()
        sys.exit()
    return finalResult
