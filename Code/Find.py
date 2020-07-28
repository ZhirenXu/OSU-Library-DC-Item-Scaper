from Code import SimpleCSV
import sys
## find and store all contents of desired <li> tags according to categoryList
# @param    source
#           html page that has been parsed by beautifulsoup
# @param    attributeList
#           a list contain 'class' attribution in <li> tag, use it to find correct <li> tag and its content
# @param    ID
#           file id for all items under this url
# @return   combinedResult
#           [[title, item title, date, visibility], [...], [...]]  
def findCategoryValue(source, attributeList, ID):
    content = ""
    combinedResult = []
    numOfAttrib = len(attributeList)
    value = []
    valueList = []
    idList = []
    i = 0
    
    listOfResult = extractValue(source, attributeList)
    lenOfResult = len(listOfResult)
    #print(lenOfResult)
    # for situation when there is only one recordw, which will add
    # same numof element as attribs number.
    if(lenOfResult == 1):
        numOfRecords = 1
    else:
        numOfRecords = len(listOfResult[0])
    while(i < numOfRecords):
        idList.append(ID)
        i = i + 1
    listOfResult.insert(0, idList)
    combinedResult = zipList(listOfResult)
    
    return combinedResult

## extract info from parsed html
# @param    source
#           parsed html by bs4
# @param    attributeList
#           A list of attributes that needed to extract info
# @return   valueList
#           [[attrib1], [attrib2], [attrib3], [...], ...]
def extractValue(source, attributeList):
    content = ""
    value = []
    valueList = []
    singleItemList = []
    
    for attrib in attributeList:
        result = source.find_all('td', attrs={'class': attrib})
        # use ; to isolate multiple li tag contents
        if len(result) > 1:
            while len(result) > 0:
                if result[0] is not None:
                    rawContent = result[0].text
                    index = rawContent.find('\r\n')
                    if index != -1:
                        content += rawContent[:index]
                    else:
                        if(rawContent == ''):
                            rawContent = "null"
                        content += rawContent
                    value.append(content)
                    content = ""
                    result.pop(0)
                else:
                    value.append("None")
            valueList.append(value)        
            value = []
        elif len(result) == 1:
            singleItemList.append(result[0].text)
        else:
            singleItemList.append("null")
    if(len(singleItemList) > 0):
        valueList.append(singleItemList)
    #print(valueList)
    return valueList

## zip the result together to get correct list for each item
# @param    target
#           [[attrib1], [attrib2], [attrib3], [...], ...]
# @return   combined
#           [[title, item title, date, visibility], [...], [...]]  
def zipList(target):
    zippedElement = []
    combined = []
    #print(target)

    # When there is only one id one record
    if(len(target) == 2):
        while(len(target) > 0):
            try:
                zippedElement.append(target.pop(0)[0])
            except:
                print("ERROR: ", target)
                sys.exit(0)
    else:
        while(len(target) > 0):
            for singleList in target:
                if (len(singleList) == 0):
                    target.remove(singleList)
                    break
                try:
                    zippedElement.append(singleList.pop(0))
                    #print(singleList)
                except:
                    print("ERROR: ", target)
                    sys.exit(0)
            #print(zippedElement)
            combined.append(zippedElement)
            zippedElement = []

    return combined
