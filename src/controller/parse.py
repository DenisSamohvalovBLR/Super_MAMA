import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()


def get_data():
    response = requests.get(
        url='https://by.detmir.com/catalog/index/name/sortforsale/is_sale/1/categories-44050',
        headers={'user-agent': f'{ua.random}'})

    with open('data/index.html', 'w') as file:
        file.write(response.text)

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

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    with open('data/result.json') as file:
        all_categories = json.load(file)
    print(all_categories)


def main():
    get_data()


if __name__ == '__main__':
    main()
