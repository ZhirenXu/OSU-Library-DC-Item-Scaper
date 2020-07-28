import sys

## print program info
def showInfo():
    print("******************************")
    print("*  DC Item Scrapper v1.0.1  *")
    print("*     Author: Zhiren Xu      *")
    print("*  published data: 7/20/20   *")
    print("******************************")

## print exit message
# @param    fileOut
#           name of output file
def sysExit(fileOut):
    print("\nThe program is finished. The output file is: ", fileOut, " . It is located in the same folder with your DC Item Scrapper program. Press enter to exit.")
    key = input()
    sys.exit()
