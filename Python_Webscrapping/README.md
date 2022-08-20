# «Web-scrapping»

Let's try to get the latest articles from [habr](https://habr.com) :)

You need to scrape the page with the latest articles ([this one](https://habr.com/ru/all/)) and select those articles, with at least one keyword (set those words in the beginning of the script). 
Print result in following format: <date> - <header> - <link>.

Example preview:

![](preview.png)

```python

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
`