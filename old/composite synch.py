import requests
from bs4 import BeautifulSoup
import re
import json
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
password = ''
payload = {'client_id': client_id, 'client_secret': client_secret, 'username': username,'password': password}
reqPost = requests.post(url, params=payload)
stuff = json.loads(reqPost.text)
token = stuff['access_token']
bearer = 'Bearer ' + token
sobj='Discovery__c'
newUrl = stuff['instance_url']+'/services/data/v54.0/composite/tree/'+sobj

counter=0
counterResult=0
toW = '{"records":['
for i in data:
    if i != None:
        if counter==50:
            toW=toW[:len(toW)-1]+']}'
            ins = requests.post(newUrl, headers={'Authorization': bearer}, json = json.loads(toW))
            print(ins.status_code,ins.content)
            inss=requests.post(url=stuff['instance_url']+'/services/data/v54.0/sobjects/Results__c', headers={'Authorization': bearer} ,json = json.loads('{"Name":"'+str(today)+'-'+str(counterResult)+'","Status__c":"'+str(ins.status_code)+'"}'))
            print(counterResult, 'Result', inss.status_code)
            counter=0
            counterResult+=1
            toW = '{"records":['
        
        tmp=i.split(',')
        toW+='{"attributes":'+'{"type" : "'+sobj+'", "referenceId" : "'+str(tmp[0])+'"},'
        toW+='"Link__c":"'+str(tmp[1])+'",'
        toW+='"MyId__c":"'+str(tmp[0])+'",'
        toW+='"Type__c":"'+'Website'+'",'
        toW+='"Name":"'+str(tmp[2])+'"},'
        counter+=1
toW=toW[:len(toW)-1]+']}'

ins = requests.post(newUrl, headers={'Authorization': bearer}, json = json.loads(toW))
print(ins.status_code)
inss=requests.post(url=stuff['instance_url']+'/services/data/v54.0/sobjects/Results__c', headers={'Authorization': bearer} ,json = json.loads('{"Name":"'+str(today)+'-'+str(counterResult)+'","Status__c":"'+str(ins.status_code)+'"}'))
print('Result',counterResult, inss.status_code)
#ff=open("csv.csv",'w')
#for i in data:
#    if i != None:
#        ff.write(i+'\n')
#ff.close()