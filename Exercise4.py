## Part 1) Implement a program that reads the content of a Wireshark (https://www.wireshark.org)
## output file into memory (dictionaries). Run Wireshark in your computer and produce a CSV file. 
## Alternatively download an example file from here https://www.ee.ucl.ac.uk/⇠mrio/ws.csv

## Part 2)  Write a python program that takes the dictionary in the previous exercise and prints 
## the list of flows in the file. For every flow you print the IP source and destination, TCP port 
## and destination and total number of bytes. In the file each row is a packet. A flow is a set 
## of packets with the same IP source, IP destination, TCP source port and TCP destination port 
## (rows 3,4,6 and 7)
import csv

with open('ws.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    csvDict = {}
    for row in readCSV:
        keys = row[0]
        csvDict[keys] = row[1:]
csvfile.close()
#print(csvDict)
    
def printFlows(tcpDict):
    # Define the new dictionary for just the TCP packets
    new_Dict = {}
    for keys, value in tcpDict.items():
        if ('>' in value[5]):
            new_Dict[keys] = value
    return new_Dict

new_Dict = printFlows(csvDict)
#print(new_Dict)

# Construct dictionary with keys and the corresponding values of IP TCP and byte length
def sameFlows(tcpFlow):
    # Define the new dictionary for the same flows
    TCPIP = {}
    for key, value in tcpFlow.items():
        TCP = [int(i) for i in value[5].split() if i.isdigit()]

        # Group the TCP source and destination port and IP source and destination port into a key
        info = (value[1],value[2],TCP[0],TCP[1])
        byte = value[4]

        # Overwrite the exisiting dictionary value with new values
        if info in TCPIP:
            TCPIP[info].append(byte)
        else:
            TCPIP[info] = [byte]
    return byte, TCP, TCPIP
            
# Construct new dictionary with similar IP and TCP port as keys and bytes length as values
def newDict(byteDict):
    # Sum the total byte length for each IP and TCP port
    byteSum = {key: sum(map(int, value)) for key, value in byteDict.items()}
    #byteSum = {key: sum(value) for key, value in byteDict.items()}
    return byteSum

# Debug purpose
info, test, haha = sameFlows(new_Dict)  
print(info)
print(type(info))
print(test)
print(type(test))
#print(test)
#print(haha)
#print(type(haha[('216.58.206.142', '10.97.172.240', 443, 54371)][1]))

totalByte = newDict(haha)
print(totalByte)
