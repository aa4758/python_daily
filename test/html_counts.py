import sys

args = sys.argv[1]
save = sys.argv[2]

with open(args, encoding='cp949') as f:
    html = f.read()

import re

body = re.search('<body.*/body>', html, re.I|re.S)
body = body.group()

body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I|re.S)
text = re.sub('<.+?>', '', body, 0, re.I|re.S)
nospace = re.sub('&nbsp;| |\t|\r|\n', '', text)

with open(save, 'w') as fu:
    fu.write(f'html = {len(html)}, text = {len(text)}, word = {len(text.split())} nospace = {len(nospace)}')

print (f'news.html = {len(html)}, text = {len(text)}, word = {len(text.split())} nospace = {len(nospace)}')