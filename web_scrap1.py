import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.karaca.com/oda-halisi"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all("div", class_="productWrap")

with open('listeler.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Tilt', 'Price']
    thewriter.writerow(header)
    for list in lists:
        tilt = list.find('span', class_='title').text.replace('\n', '')
        price = list.find('span', class_='prices').text.replace('\n', '')
        info = [tilt, price]
        thewriter.writerow(info)
