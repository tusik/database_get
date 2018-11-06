import requests,os
from bs4 import BeautifulSoup

url="https://cdn.databases.today/"
rurl="http://cdn.databases.today/random/"
req = requests.post(url).text
soup = BeautifulSoup(req,'html.parser')
file_list=soup.find_all('a')

reqr = requests.get(rurl).text
soupr = BeautifulSoup(reqr,'html.parser')
rand_list=soupr.find_all('a')

for i in range(0,len(rand_list)):
    if(rand_list[i]['href'].find('.')>-1):
        print(rand_list[i]['href'])
        os.system('wget -P random/ '+rurl+'/'+rand_list[i]['href'])

for i in range(0,len(file_list)):
    if(str(file_list[i]['href']).find('cdn.databases.today/')>-1):
        print(file_list[i]['href'])
        os.system('wget '+file_list[i]['href'])
