import requests
import sys
from bs4 import BeautifulSoup



google_url = 'https://www.ptt.cc/bbs/NBA/index.html'
my_params = {'q': '日期'}

r = requests.get(google_url, params = my_params)

if r.status_code == requests.codes.ok:
  soup = BeautifulSoup(r.text, 'html.parser')
  print(soup.prettify())
    
articles = []  # 儲存取得的文章資料
divs = soup.find_all('div', 'r-ent')
for d in divs:          	
    if d.find('a'): 
      href = d.find('a')['href']
      title = d.find('a').string
      author = d.select('div.meta > div.author')
      for i in author:
        name = i.text
      d = d.select('div.date')
      for i in d:
        date = i.text
      articles.append({
        '標題': title,
        'href': href,
        '作者':name,
        '日期':date,
      })
print (articles)
    
