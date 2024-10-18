import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://wavu.wiki/t/Paul_movelist')
paulmovesTxt = open("paulMovelistHTML.txt", 'a')


print(r)
soup = BeautifulSoup(r.content, 'html.parser')
#paulMovesHtml = soup.find_all('div', class_ = "movedata hover-bg-grey-03 mw-collapsible mw-collapsed")

#paulMovesHtml = soup.find_all(id = 'Paul-2+3')
paulMovesHtml = soup.find_all(id = re.compile("Paul-*"))
i = 0
for tag in paulMovesHtml:
    print(tag)
    print(i)
    i = i + 1
print(type(paulMovesHtml))
#paulmovesTxt.write(paulMovesHtml)
