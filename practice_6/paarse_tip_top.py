import requests
from bs4 import BeautifulSoup as BS

page = requests.get('https://tiptop.ua/shop/televizory-lcd-plasma-led')

# print(page.text)
bs = BS(page.text, "html5lib")

dd = bs.findAll("div", {"class": "product__item--inner"})

# print(bs.text)
urls = []

for d in dd:
    urls.append(d.a['href'])

for u in urls:
    page = requests.get(u)
    bs_obj = BS(page.text, "html5lib")

    h1 = bs_obj.find('h1', {'class': "site__title"})
    name = h1.get_text().replace("\\n", "").strip()

    div = bs_obj.find('div', {"class": "product__item--price"})
    price = div.get_text().replace("\\n", "").strip()

    print(f"{name} ===>> {price}")
