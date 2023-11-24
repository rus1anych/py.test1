from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs

page_url = 'https://stepik.org/media/attachments/lesson/209723/3.html'


def get_html(url):
    response = urlopen(url)
    html = response.read().decode('utf8')
    return html

def parse_html(html):
    soup = Bs(html, 'html.parser')
    summ = 0
    for td in soup.find_all('td'):
        number = int(td.get_text())
        summ = summ + number

    print(summ)

def main():
    parse_html(get_html(page_url))


if __name__ == '__main__':
    main()