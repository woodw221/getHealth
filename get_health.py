import yaml
import requests
import time
import os
from collections import Counter
from pathlib import Path

# Check to see if the website is UP
def getHealth(hRequest):
    wUrl = hRequest.get('url')
    wHeaders = None
    wBody = None
    wMethod = 'GET'

    if hRequest.get('method') is not None:
        wMethod = hRequest.get('method')
    
    if hRequest.get('headers') is not None:
        wHeaders = hRequest.get('headers')
    
    if hRequest.get('body') is not None:
        wBody = hRequest.get('body')
    
    getResponse = requests.request(method=wMethod, url= wUrl, headers=wHeaders, data=wBody)

    if getResponse.status_code >= 200 and getResponse.status_code <= 299 and getResponse.elapsed.total_seconds() <= 0.5 :
        return('UP')
    else :
        return('DOWN')  

def calcUpStats(success, total):
    if total == 0:
        return 0
    perc = 100 * (success/total)
    return perc


user_input = Path(input("Please enter the path of the yaml file: "))

if os.path.exists(user_input):
    with open(user_input) as f:
        result = yaml.safe_load(f)
    
    unique = []
    unique.append(result[0]['name'].split(' ', 1)[0])

    # Figure out unique domains through names
    # Assume domain is the first part of name
    for x in result :
        if not x['name'].split(' ', 1)[0] in unique:
            unique.append(x['name'].split(' ', 1)[0])

    successCnt = Counter()
    checkCount = Counter()

    
    try:
        while True:

            for x in result:
                status = getHealth(x)
                if status == 'UP':
                    successCnt[x['name'].split(' ', 1)[0]] += 1
        
                checkCount[x['name'].split(' ', 1)[0]] += 1

            time.sleep(15)
    except KeyboardInterrupt:
        for x in unique:
            if checkCount[x] == 0:
                print('Program did not check status for ' + x)
            else:
                upPerc = calcUpStats(successCnt[x], checkCount[x])
                print(x + ' has ' + "%.0f%%" % (upPerc) + ' availibility percentage')

else:
    print("File does not exist")
