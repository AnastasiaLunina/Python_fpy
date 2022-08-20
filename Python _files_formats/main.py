import collections
import json
from pprint import pprint


def read_json(file_path, max_len_words=6, top_words=10):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = [] #save all words from news to this list
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_words] 
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        pprint(counter_words.most_common(top_words))

if __name__ == '__main__':
    read_json('newsafr.json')