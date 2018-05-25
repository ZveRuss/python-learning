import urllib

url = 'http://yandex.ru'
html = urllib.urlopen(url).read()


f = open('index.html', 'w')
f.write(html)