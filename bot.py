from bs4 import BeautifulSoup
import requests
import re
import time

page = 'https://ww1.mangakakalots.com/chapter/yx917940/chapter_'
i = 1
while True:
    try:
        html = requests.get(page + str(i))
    except Exception as ex:
        print(ex)
        break

    soup = BeautifulSoup(html.content, 'html.parser')
    new_html = ''

    for line in soup.find_all('div', class_ = 'vung-doc'):
        new_html += str(line)

    with open('chapters_html/chapter ' + str(i) + ' colored.html', 'w') as html_file:
        html_file.write(new_html)

    print('chapter ' + str(i) + ' downloaded')
    i += 1
    time.sleep(1)