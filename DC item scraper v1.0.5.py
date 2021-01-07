from Code import Greeting
from Code import SimpleCSV
from Code import Run
import concurrent.futures
from Code import Login
from Code import ItemAttribute
from Code import ItemHeader

def main(*argv):
    itemURL = []
    idList = []
    csvIn = ""
    csvOut = ""
    liTagList = []

    Greeting.showInfo()
    #argv is used to remember if user want login. Null means no-login
    logSession = Login.login()
    header = ItemHeader.getItemHeader()
    csvIn = SimpleCSV.getCSVInput()
    csvOut = SimpleCSV.getCSVOutput()
    #TODO: ask user to choose colomn
    #now just get first colomn, parent id
    urlList = SimpleCSV.readColomn(csvIn, 0)
    # open file for output
    outFile = open(csvOut, 'w', encoding = 'utf8', newline='')
    SimpleCSV.writeCSV(header, outFile)
    attributeList = ItemAttribute.getItemAttribute()
    if logSession == ():
        Run.runProcessParallel(itemURL, attributeList, outFile, numOfUrl)
    else:
        Run.runProcessParallelLogin(logSession, urlList, attributeList, outFile)
    outFile.close()
    Greeting.sysExit(csvOut)
    
if __name__ == "__main__":
    main()
