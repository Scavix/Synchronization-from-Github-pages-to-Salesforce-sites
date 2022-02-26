import requests
from bs4 import BeautifulSoup
import re
import json
import time
from datetime import datetime

today = datetime.now()
data=[]
#data.append('Id,Link,Name,Important')
#vals=['Id','Link','Name','Important']
URL = "https://scavix.github.io/cs_resources.html"
reqGet = requests.get(URL)
idc=1
#print(page.text)
soup = BeautifulSoup(reqGet.content, "html.parser")
#print(soup.find_all("li"))
for i in str(soup.find_all("body")).split('\n'):
    x = re.search("<a href=\"(.*)\">(.*)<\/a>.*",str(i))
    if x:        
        if x.group(2)!='':
            if '<b>' in x.group(2):
                data.append(str(idc)+','+x.group(1)+','+x.group(2)[3:-4].replace(',','')+','+str(1))
            else:
                data.append(str(idc)+','+x.group(1)+','+x.group(2).replace(',','')+','+str(0))
            idc+=1

url = 'https://login.salesforce.com/services/oauth2/token?grant_type=password'
client_id = ''
client_secret = ''
username = ''
st=''
pw=''
password = pw+st

payload = {'client_id': client_id, 'client_secret': client_secret, 'username': username,'password': password}
reqPost = requests.post(url, params=payload)
stuff = json.loads(reqPost.text)
token = stuff['access_token']
bearer = 'Bearer ' + token
sobj='Resource__c'
extField='MyId__c'
newUrl = stuff['instance_url']+'/services/data/v54.0/sobjects/'+sobj+'/'+extField+'/'


for i in data:
    if i != None:
        tmp=i.split(',')
        toW='{"Link__c":"'+str(tmp[1])+'",'
        toW+='"Categories__c":"Computer Science",'
        #toW+='"MyId__c":"'+str(tmp[0])+'",'
        toW+='"Important__c":'+('"true"' if tmp[3]=='1' else '"false"')+','
        toW+='"Name":"'+str(tmp[2])+'"}'
        ins=requests.patch(newUrl+str(tmp[0]), headers={'Authorization': bearer}, json = json.loads(toW))
        print(ins.status_code,ins.content)
        time.sleep(1)

data=[]
URL = "https://scavix.github.io/math_resources.html"
reqGet = requests.get(URL)
soup = BeautifulSoup(reqGet.content, "html.parser")
for i in str(soup.find_all("body")).split('\n'):
    x = re.search("<a href=\"(.*)\">(.*)<\/a>.*",str(i))
    if x:
        if x.group(2)!='':
            if '<b>' in x.group(2):
                data.append(str(idc)+','+x.group(1)+','+x.group(2)[3:-4].replace(',','')+','+str(1))
            else:
                data.append(str(idc)+','+x.group(1)+','+x.group(2).replace(',','')+','+str(0))
            idc+=1

for i in data:
    if i != None:
        tmp=i.split(',')
        toW='{"Link__c":"'+str(tmp[1])+'",'
        toW+='"Categories__c":"Mathematics",'
        toW+='"Important__c":'+('"true"' if tmp[3]=='1' else '"false"')+','
        toW+='"Name":"'+str(tmp[2])+'"}'
        ins = requests.patch(newUrl+str(tmp[0]), headers={'Authorization': bearer}, json = json.loads(toW))
        print(ins.status_code,ins.content)
        time.sleep(1)


#ff=open("csv.csv",'w')
#for i in data:
#    if i != None:
#        ff.write(i+'\n')
#ff.close()