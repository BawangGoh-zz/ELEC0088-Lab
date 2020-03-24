import csv
import numpy as np 

class ClassPacket:
	def __init__(self, filename):
		self.filename = filename

	def openFile(self):
		with open(self.filename, 'r') as csvfile:
		    readCSV = csv.reader(csvfile, delimiter = ',')
		    csvDict = {}
		    for row in readCSV:
		        keys = row[0]
		        csvDict[keys] = row[1:]
		csvfile.close()

		return csvDict

	def printFlow(self, tcpDict):
	    new_Dict = {}
	    for keys, value in tcpDict.items():
	        if ('>' in value[5]):
	            new_Dict[keys] = value

	    return new_Dict


	def sameFlow(self, tcpFlow):
	    TCPIP = {}
	    for key, value in tcpFlow.items():
	        TCP = [int(i) for i in value[5].split() if i.isdigit()]
	        info = (value[1],value[2],TCP[0],TCP[1])
	        byte = value[4]
	        if info in TCPIP:
	            TCPIP[info].append(byte)
	        else:
	            TCPIP[info] = [byte]

	    return TCPIP

	def newDict(self, byteDict):
	    byteSum = {key: sum(map(int, value)) for key, value in byteDict.items()}

	    return byteSum