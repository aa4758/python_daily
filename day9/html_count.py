{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "news.html = 202293, text = 54745, word = 1579 nospace = 5747\n"
     ]
    }
   ],
   "source": [
    "with open('news.html', encoding='cp949') as f:\n",
    "    html = f.read()\n",
    "\n",
    "import re\n",
    "\n",
    "body = re.search('<body.*/body>', html, re.I|re.S)\n",
    "body = body.group()\n",
    "\n",
    "body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I|re.S)\n",
    "text = re.sub('<.+?>', '', body, 0, re.I|re.S)\n",
    "nospace = re.sub('&nbsp;| |\\t|\\r|\\n', '', text)\n",
    "\n",
    "with open('result.txt', 'w') as fu:\n",
    "    fu.write(f'html = {len(html)}, text = {len(text)}, word = {len(text.split())} nospace = {len(nospace)}')\n",
    "\n",
    "print (f'news.html = {len(html)}, text = {len(text)}, word = {len(text.split())} nospace = {len(nospace)}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
