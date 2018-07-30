from bs4 import BeautifulSoup


import requests

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(r.text, 'html.parser')

result = soup.find('div', {"class": "mw-parser-output"})
x = result.find_all('ul')
z = x[14].find_all('li')

for t in z:
    print(t.find('a'))
