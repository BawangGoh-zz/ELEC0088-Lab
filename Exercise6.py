# Exercises
# Use Pandas to process and query the wireshark ﬁle you used in Chapter 6 
import numpy as np 
import pandas as pd
from ImportClass import ClassPacket

def loadPacket():
	df = pd.read_csv("ws.csv")
	df.index = df.index + 1
	print(df.head())

	return df

def insertColRow(packetDF):
	n_row = packetDF.shape[0]
	new_row = packetDF.loc[n_row]
	packetDF.loc[n_row+1,:] = new_row

	new_col = packetDF.loc[:, 'Time']*packetDF.loc[:, 'Length']
	name_col = 'Test'
	packetDF.insert(packetDF.shape[1], name_col, new_col)
	print(packetDF)

	return packetDF

def main():
	# Part 1) Load the Wireshark ﬁle that you used in chapter 6 into a pandas DataFrame
	df = loadPacket()

	# Part 2) How many packets (rows) are there in the DataFrame?
	# Print the number of packet
	num_packet = df.shape[0]
	print('Number of packets: ' + str(num_packet))

	# Part 3) How many ﬁelds (columns) are there in the DataFrame?
	print(df.keys())
	num_field = df.shape[1]
	print(num_field)

	# Part 4) Remove the last column from DataFrame
	df.drop('Info', axis=1, inplace=True)
	print(df)

	# Part 5) Insert a row/column
	df = insertColRow(df)

	# Part 6) What is the maximun length of a packet?
	max_len = df['Length'].max()
	print(max_len)

	# Part 7) What is the mean length of TCP packets?
	mean_len = df['Length'].mean()
	print(mean_len)

	# Part 8) Repeat the exercise 6.2 with pandas
	# Pipeline for filtering TCP flow
	PacketObj = ClassPacket('ws.csv')
	packetDict = PacketObj.openFile()
	packetFlow = PacketObj.printFlow(packetDict)
	tcpFlow = PacketObj.sameFlow(packetFlow)
	tcpByte = PacketObj.newDict(tcpFlow)

	# Convert to pandas Dataframe
	tcpDF = pd.DataFrame([[keys[0], keys[1], keys[2], keys[3], values] for keys, values in tcpByte.items()]) \
            .rename(columns={0:'IP source', 1:'IP destination', 2:'TCP source', 3:'TCP destination', 4:'Byte length'})
	print(tcpDF)

if __name__== "__main__":
	main()

