import requests
from bs4 import BeautifulSoup

def getData (symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    url = 'https://finance.yahoo.com/quote/{}/'.format(symbol)
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
    percentage = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text

    stock = {
        'symbol' : symbol,
        'Price' : price,
        'Change' : change,
        'percentage' : percentage
    }
    
    return stock


name = input("Enter Stock Symbol: ")
print("Stock: ", name)
print(getData(name))
