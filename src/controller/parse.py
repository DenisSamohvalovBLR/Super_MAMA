import requests
from bs4 import BeautifulSoup


def get_data():
    headers = {
        'user-agent': 'Mozilla / 5.0(X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 97.0 .4692 .71 Safari / 537.36'
    }

    r = requests.get(url='https://by.detmir.com/catalog/index/name/sortforsale/is_sale/1/categories-44050',
                     headers=headers)

    with open('data/index.html', 'w') as file:
        file.write(r.text)

    with open('data/index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    title = soup.find_all('p', class_='GT')
    discount = soup.find_all('p', class_='G_3')
    link = soup.find('div', class_='lS').find_all('a')

    result = []
    i = 0
    if len(title) == len(discount):
        for el in title:
            result.append(f"{el.text} : {discount[i].text} : {link[i]['href']}")
            i += 1

    for el in result:
        print(el)


def main():
    get_data()


if __name__ == '__main__':
    main()
