import csv
import unittest
import source.readCSVtoDict

def test_readcourierCSVtoDict():
    result = [{"Name": "Raymond", "Phone": "0789887889"},
              {"Name": "Addison", "Phone": "0765345321"},
              {"Name": "Peter", "Phone": "07625435678"}]
    
    
    
    assert source.readCSVtoDict.readcourierCSVtoDict() == result
    
test_readcourierCSVtoDict()
    

    