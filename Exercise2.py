## Part 1) Implement a DNS querying program that stores the mapping between the names
## into IP addresses. Explicitly define the name of the network into the databases
## Part 2) Allow for the user to query several types of NS record (NS, MX, etc).
# IP addresses query
def IPquery(dct, string):
    return dct.get(string)

def NS_MX(dct, string):
    if(string.find('NS') == True):
        print(str(dct.get(string)))
    else:
        print(str(dct.get(string)))

def main():
    ## Part 1) Defining DNS query name and IP addresses databases
    IPdatabase = {"www.ee.ucl.ac.uk": '144.82.8.143',
                "www.google.com": '8.8.8.8'}
    website = str(input("Enter a website: "))
    print("Requested IP address: " + IPquery(IPdatabase, website))
    print("Print all records: ")
    print (IPdatabase)

    ## Part 2) Defining DNS query name and IP addresses for NS and MX databases
    lookup = {'NS': {"www.bbc.co.uk": '212.58.244.26'},
            'MX': {"www.google.com": '173.194.202.27'}}
    dnstype = str(input("Enter type of lookup: "))
    NS_MX(lookup, dnstype)
    
if __name__ == "__main__":
    main()