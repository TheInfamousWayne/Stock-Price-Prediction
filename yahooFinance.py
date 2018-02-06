from urllib.request import urlopen
from bs4 import BeautifulSoup

optionsUrl = 'http://finance.yahoo.com/q/op?s=AAPL+Options'
optionsPage = urlopen(optionsUrl)
soup = BeautifulSoup(optionsPage, 'lxml')
soup.find_all(title='AAPL180105C00130000')
