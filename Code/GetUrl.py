
## Use input id to generate url list for collection(parent)
# @param    idList
#           A list contain all parent ids
# @return   urlList
#           A list contain all parent urls
def generateParentUrl(idList):
    prefix = "https://library.osu.edu/dc/concern/generic_works/"
    urlList = []
    url = ""

    # ids is a list
    for ids in idList:
        for itemId in ids:
            url = prefix + itemId
            urlList.append(url)

    return urlList

## Use input id to generate url List for related item
# @param    parentIdList
#           A parent id
# @param    itemIdList
#           A list contain all item ids (file_set_id)
# @return   urlList
#           A list contain all item urls
def generateItemUrl(parentId, itemIdList):
    prefix = "https://library.osu.edu/dc/concern/parent/"
    interim = "/file_sets/"
    url = ""
    urlList = []
    for itemIds in itemIdList:
        for itemId in itemIds:
            url = prefix + parentId + interim + intemId
            urlList.append(url)

    return urlList
            

    
