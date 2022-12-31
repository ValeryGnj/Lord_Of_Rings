import requests as rq
import json
# Получаем список книг с сайта
url = 'https://the-one-api.dev/v2/book'
r = rq.get(url)
d = json.loads(r.text)
list_book = d['docs']
# Обрабатываем список для доступа к страницам с главами
data = []
data1 = []
for item in list_book:
    data.append(item['_id'])
    data1.append(item['name'])
# Получаем список глав для каждой книги
data2 = []
for (index, _) in enumerate(data):
    url = 'https://the-one-api.dev/v2/book/' + data[index] + '/chapter'
    r = rq.get(url)
    d = json.loads(r.text)
    list_chapterName = d['docs']
    data2.append(list_chapterName)
    for index in list_chapterName:
        del index['_id']
# Выводим древовидную структуру книг
new_data = dict(zip(data1, data2))
new_json = json.dumps(new_data, indent=4)
print(new_json)
