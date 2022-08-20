import json
from pprint import pprint
import requests
from datetime import datetime, timedelta, timezone


def decor_logger(file_name):
    def decor(old_function):
        def new_function(*args, **kwargs):
            function_start = datetime.today()
            function_name = old_function.__name__
            with open(file_name, "a", encoding="UTF-8") as file:
                file.write(f"On {function_start} Called function: {function_name} \n")
                result = old_function(*args, **kwargs)
                file.write(f"With following results: {result} \n")
            return result
        return new_function
    return decor


# Decorating the function from Stackoverflow HW
@decor_logger("log.txt")
def get_stackoverflow():
    tag = 'python'
    pagesize = 100
    base_url = 'https://api.stackexchange.com/'
    sort = 'desc'

    date_to = datetime.now()
    date_from = (date_to - timedelta(2)).strftime('%d/%m/%Y')
    date_to = date_to.strftime('%d/%m/%Y')
    print(f'Questions asked on Stackoverflow from {date_from} to {date_to} containing tag {tag}:')

    # Converting date to UNIX format for URL
    date_to = round(datetime.strptime(date_to, "%d/%m/%Y").replace(tzinfo=timezone.utc).timestamp())
    date_from = round(datetime.strptime(date_from, "%d/%m/%Y").replace(tzinfo=timezone.utc).timestamp())

    url_questions = f'{base_url}/2.3/questions?pagesize={pagesize}&fromdate={date_from}&todate={date_to}&order={sort}&sort=creation&tagged={tag}&site=stackoverflow'

    response = requests.get(url_questions, timeout=10)
    response.raise_for_status()

    if response.status_code == 200:
        print('Success')

    response = response.json()
    response_dict = response.get('items')
    response_title = [d['title'] for d in response_dict]
    pprint(response_title)
    return response_title


if __name__ == '__main__':
    get_stackoverflow()

