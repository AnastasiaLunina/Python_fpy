from pprint import pprint
import requests


def heroes():
    url = 'https://superheroapi.com/api/'
    token = 2619421814940190
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    intelligence = []

    for hero_name in heroes_list:
        response = requests.get(f"{url}{token}/search/{hero_name}")
        results = response.json().get("results")

        for result_list in results:
            if result_list['name'] in heroes_list:
                superhero_id = result_list['id']

        response = requests.get(f"{url}{token}/{superhero_id}/powerstats")
        results_list = []
        for each in response:
            results_list.append(each)

        results = int(response.json()["intelligence"])
        intelligence.append(results)

    heroes_intelligence = list(zip(heroes_list, intelligence))
    most_intelligent = sorted(heroes_intelligence, key=lambda x: x[1], reverse=True)[0]
    print(f'The most intelligent superhero is {most_intelligent}.')


heroes()
