##Return a list of item meta we want to put in csv file
# @return   itemMeta
#           The list contain all category name
#tag is td, attr is class
def getItemAttribute():
    itemAttribute = ["attribute attribute-filename ensure-wrapped",
                     "attribute attribute-date_uploaded",
                     "attribute attribute-permission"]
    #multithread return print out in wrong order
    test = ["attribute attribute-date_uploaded"]
    return itemAttribute
