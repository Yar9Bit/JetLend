import requests
from bs4 import BeautifulSoup

url = 'https://jetlend.ru/borrower/'
resp = requests.get(url)

soup = BeautifulSoup(resp.content, 'html5lib')


def len_all_html_tag():
    tag = [t.name for t in soup.find_all(True)]
    return len(tag)


def len_html_has_attr():
    attrs = [t.attrs for t in soup.find_all(True)]
    return len(attrs)


if __name__ == '__main__':
    print(len_all_html_tag())
    print(len_html_has_attr())
