import re
idc=1
toSync=[]
data=[]
toSync.append('Id,Link,Name,Important')
f=open('cs.html','r')
for i in f:
    data.append(i)

for i in data:
    x = re.search("<a href=\"(.*)\">(.*)<\/a>.*",i)
    if x:        
        if x.group(2)!='':
            if '<b>' in x.group(2):
                toSync.append(str(idc)+','+x.group(1)+','+x.group(2)[3:-4].replace(',','')+','+str(1))
            else:
                toSync.append(str(idc)+','+x.group(1)+','+x.group(2).replace(',','')+','+str(0))
            idc+=1

ff=open("csv.csv",'w')
for i in toSync:
    if i != None:
        ff.write(i+'\n')
ff.close()