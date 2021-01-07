## find object title and handler, then store it into a list
# @param    source
#           html page that has been parsed by beautifulsoup
# @param    valueList
#           a list contain contents in each <li> tag, in here we just need to add item's title
def findObjectTitle(source):
    value = "null"
    # delete front/back whitespace and add to valueList
    tag = source.find("div", "col-sm-8")
    try:
        h2 = tag.contents[1]
        #h2 is a list, format as: ['\\n', <h2>The Lantern, Ja...span></small>\n</h2>, '\\n']
        value = h2.contents[0].string
        try:
            index = value.index("\n")
            value = value[:index]
        except:
            value = value
            
    except:
        print("Fail to get record title!")


    return value
