import csv
import traceback

def readCSVtoDict():
    myList = []
    try:
        with open("data/product_list.csv", mode = "r") as csvFile:
                    for line in csv.DictReader(csvFile):
                        myList.append(line)
                        
        return myList
    
    except:
        traceback.print_exc()
        
def readcourierCSVtoDict():
    myList = []
    try:
        with open("data/courier_list.csv", mode = "r") as csvFile:
                    for line in csv.DictReader(csvFile):
                        myList.append(line)
                        
        return myList
    
    except:
        traceback.print_exc()

def readorderCSVtoDict():
    myList = []
    try:
        with open("data/order_dictionary.csv", mode = "r") as csvFile:
                    for line in csv.DictReader(csvFile):
                        myList.append(line)
                        
        return myList
    
    except:
        traceback.print_exc()
        

        
