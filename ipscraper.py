import requests
from bs4 import BeautifulSoup
import os
page = requests.get('https://mon-ip.io/')
soup= BeautifulSoup(page.text, 'html.parser')
with open('C:\\Users\\pc\\Desktop\\IP\\html.txt', 'w', encoding='utf-8') as f:
    f.write(str(soup))
ip = soup.find("p",id='ip').text
print(ip)
with open('C:\\Users\\pc\\Desktop\\IP\\IP.txt', 'w', encoding='utf-8') as f:
    f.write(ip)
fichier = r"C:\\Users\\pc\\Desktop\\IP\\IP.txt"
os.system(f'notepad {fichier}')