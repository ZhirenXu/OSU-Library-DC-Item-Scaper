import urllib.request
import concurrent.futures
from bs4 import BeautifulSoup
from Code import FindObjectTitle
from Code import Find
from Code import GetUrl
import requests
from Code import SimpleCSV
from requests import Session

def loadUrl(url):
    html = urllib.request.urlopen(url)
    return html

def loadUrlSession(session, url):
    html = session.get(url)
    return html

##main process of the metadata scrapper
# @param    urlList
#           a list contains url that wait to be scrapped
# @param    liTagList
#           A list contain all the <li> tag we need
# @param    outputFile
#           a CSV file for output
# @param    numOfUrl
#           How many url need to be scraped
def runProcessParallel(urlList, liTagList, outputFile, numOfUrl):
    # iterator to show program progress
    categoryValue = []
    i = 1
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 12) as executor:
        future_to_url = {executor.submit(loadUrl, url): url for url in urlList}
        for future in concurrent.futures.as_completed(future_to_url):
            # original url link
            url = future_to_url[future]
            # opened url
            html = future.result()
            # load target digital collection in html parser
            soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
            # find collection title
            FindObjectTitle.findObjectTitle(soup, categoryValue)
            # find original url link
            categoryValue.append(url)
            # find attributes value
            proto_Find.findCategoryValue(soup, liTagList, categoryValue, outputFile)
            print("We have successfully web-scraped ", i, " / ", numOfUrl, " records")
            # reset categoryValue for next collection
            categoryValue = []
            i = i + 1

##main process of the metadata scrapper with login session
# @param    session
#           a session which contain login cookie
# @param    urlList
#           a list contain item url
# @param    attributeList
#           A list contain all the <td> attributes we need
# @param    outputFile
#           a CSV file for output
def runProcessParallelLogin(session, urlList, attributeList, outputFile):
    # iterator to show program progress
    categoryValue = []
    i = 1

    #urlList = GetUrl.generateParentUrl(idList)
    numOfUrl = len(urlList)
    print("There are ", numOfUrl, " records in the input file.\n")
    print("Proceeding......\n")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 12) as executor:
        future_to_url = {executor.submit(loadUrlSession, session, url): url for url in urlList}
        for future in concurrent.futures.as_completed(future_to_url):
            print("Processing ",i, " / ", numOfUrl, "records.")
            # original url link
            url = future_to_url[future]
            ID = url[(len(url) - 9):]
            # opened url
            html = future.result()
            # load target digital collection in html parser
            soup = BeautifulSoup(html.text, 'html.parser')
            #print(nextPageUrl)
            # find collection title
            title = FindObjectTitle.findObjectTitle(soup)
            # find attributes value
            categoryValue = Find.findCategoryValue(soup, attributeList, ID)
            #print(categoryValue)
            generateOutput(categoryValue, outputFile, title)
            nextPageSoup = findNextPage(soup, session)
            if nextPageSoup != None:
                categoryValue = Find.findCategoryValue(nextPageSoup, attributeList, ID)
                generateOutput(categoryValue, outputFile, title)
                print("All pages processed. No more next page.")
                print("Write into CSV successful.")
            else:
                print("No next page for this record")
            print("Successfully web-scraped ", i, " / ", numOfUrl, "records.\n")
            i = i + 1

## add master file name into list and write data into csv file
# @param    listOfRows
#           Expected data by row, each row is a list
# @param    output
#           Output csv file, opened
# @param    masterFileName
#           Name of the master file which contains items 
def generateOutput(listOfRows, output, masterFileName):
    #print(listOfRows)
    for row in listOfRows:
        row.insert(1, masterFileName)
        #print(row)
        if len(row) > 1:
            SimpleCSV.writeCSV(row, output)

## if items are more than 9, it will continue in next page.
## find the next page and return the parsed html of next page
# @param    source
#           parsed html of master file(or previous page if there is multiple nextpage)
# @param    session
#           A web cookie object which include login info in order to get private record.
# @return   nextPageSoup
#           if there is a next page, return a parsed html of next page
#           Otherwise, return None
def findNextPage(source, session):
    nextPage = ""
    urlPrefix = "https://library.osu.edu/"
    result = source.find('a', attrs={'rel': 'next'})
    print(result)
    if (result != None):
        nextPage = urlPrefix + result['href']
        print("Next page of items is founded, processing...")
        html = loadUrlSession(session, nextPage)
        nextPageSoup = BeautifulSoup(html.text, 'html.parser')
        return nextPageSoup
    else:
        return None
