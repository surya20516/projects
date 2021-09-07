import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link=input("enter- ")
uh=urllib.request.urlopen(link)
data=uh.read()
tree=ET.fromstring(data)
results=tree.findall('comments/comment')
count=0
sum=0
for i in results:
    x=int(i.find('count').text)
    count=count+1
    sum=sum+x
print(count)
print(sum)
