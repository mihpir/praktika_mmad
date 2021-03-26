from bs4 import BeautifulSoup as bs
import codecs
import re
from collections import defaultdict
import requests
import sys

url = input('Введите URL: ') # например: https://ravesli.com/urok-1-vvedenie-v-programmirovanie/
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
f = open(r'example.html',"wb")
try:   
    ufr = requests.get(url, headers = headers)
    f.write(ufr.content)
    f.close()    
except Exception as e:
    print("Было сгенерировано исключение: " + str(e) + "\n")
    sys.exit()
finally:
    f.close()

doc = bs(codecs.open('example.html', encoding='utf-8', mode='r').read(), 'html.parser')

# извлечение данных из статьи
try:
    author = doc.select('.data')[1].decode_contents().strip()
    title = doc.select('.zagolovokstat')[0].decode_contents().strip()
    date = doc.select('.data')[2].decode_contents()
    date = re.sub(r'\<[^>]*\>', '', date)
    date = re.sub(r'\|', '', date).strip()
    view = doc.select('.catsingle')[1].decode_contents()
    view = re.sub(r'\<[^>]*\>', '', view).strip()
    rating = doc.select('.post-ratings')[0].decode_contents()
    rating = re.sub(r'\<[^>]*\>', '', rating)
    rating = re.sub(r'[()]', '', rating).strip()
except Exception:
    print("Не удалось извлечь данные из статьи по заданному шаблону.\n")
    sys.exit()
    
# вывод на экран
print('Автор:', author)
print('Заголовок:', title)
print('Дата:', date)
print('Количество просмотров:', view)
print('Рейтинг:', rating)

# извлечение данных о комментариях
comments = []
for node in doc.select('.comment-body'):
    text = node.select('p')[0].decode_contents().strip()
    text = re.sub(r'\<[^>]*\>', '', text)
    text = re.sub(r'\n', ' ', text)
    author = node.select('cite')[0].decode_contents().strip()
    comments.append({'text': text, 'author': author})

# вывод информации по комментариям
print('\nКомментариев в статье:', len(comments))
print('\nСамый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])
print('\nСамый длинный комментарий:', sorted(comments, key=lambda x: len(x['text']), reverse=True)[0]['text'])

# самый активный комментатор
commentators = defaultdict(int)
for comment in comments:
    commentators[comment['author']] += 1
    
most_active = max(commentators, key=commentators.get)
print('\nСамый активный:', most_active, ', комментариев:', commentators[most_active])