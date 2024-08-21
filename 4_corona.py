#import requests library
import requests
#define fetch function
def fetch(url):
    response=requests.get(url)
     #get status and proceed to fetch data if accessible.
    if response.status_code==200:
        data=response.json()
        #we've our content inside raw_data key so run loop through it
        for i in data['rawData']:
            #validate entries of  Canada,India,China, and Africa and print the requires data
            if(i["Country_Region"]=="Canada"):
                print(i["Country_Region"])
                print(i["Deaths"])
                print(i["Last_Update"])
            elif(i["Country_Region"]=="India"):
                print(i["Country_Region"])
                print(i["Deaths"])
                print(i["Last_Update"])
            elif(i["Country_Region"]=="China"):
                print(i["Country_Region"])
                print(i["Deaths"])
                print(i["Last_Update"])
            elif(i["Country_Region"]=="Africa"):
                print(i["Country_Region"])
                print(i["Deaths"])
                print(i["Last_Update"])
            
#make variable for url and call the function      
url="https://coronavirus.m.pipedream.net/"
fetch(url)
#print(entr)