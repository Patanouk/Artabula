import json
from typing import Dict

import requests

# Documentation
# How to search by location : https://commons.wikimedia.org/wiki/Commons:Search_by_location
# Geosearch query : https://www.mediawiki.org/wiki/Extension:GeoData#list=geosearch

WIKIMEDIA_BASE_URL = "https://commons.wikimedia.org/w/api.php?"

SEARCH_RADIUS_METERS = 500  # Distance around the coordinate we search
SEARCH_COORDINATES = '49.0222493192745|2.000689441938519'  # Coordinates around which we search, in lat|long format
NUMBER_SEARCH_RESULT = 5  # Max 500 per search


def get_wikimedia_page_id_to_url() -> Dict[str, str]:
    wikimedia_response = requests.get(f'{WIKIMEDIA_BASE_URL}'
                                      'format=json&'
                                      'action=query&'
                                      'generator=geosearch&'
                                      'ggsprimary=all&'
                                      'ggsnamespace=6&'
                                      f'ggsradius={SEARCH_RADIUS_METERS}&'
                                      f'ggscoord={SEARCH_COORDINATES}&'
                                      f'ggslimit={NUMBER_SEARCH_RESULT}&'
                                      'prop=imageinfo&'
                                      'iilimit=1&'
                                      'iiprop=url&'
                                      'iiurlwidth=200&'
                                      'iiurlheight=200')

    json_response = json.loads(wikimedia_response.text)

    pages = json_response['query']['pages']
    result = {}
    for page in pages:
        result[page] = pages[page]['imageinfo'][0]['url']

    print(f'Extracted images to page ids : {result}')

    return result


def print_wikimedia_geosearch_results() -> None:
    wikimedia_response = requests.get(f'{WIKIMEDIA_BASE_URL}'
                                      'action=query&'
                                      'format=json&'
                                      f'gscoord={SEARCH_COORDINATES}&'
                                      'gsnamespace=6&'  # Namespace 6 is the file namespace in wikimedia
                                      'gsprimary=all&'
                                      f'gsradius={SEARCH_RADIUS_METERS}&'
                                      f'gslimit={NUMBER_SEARCH_RESULT}&'
                                      'list=geosearch')

    url_dict = get_wikimedia_page_id_to_url()

    json_response = json.loads(wikimedia_response.text)
    geosearch_results = json_response['query']['geosearch']
    for geosearch_result in geosearch_results:
        geosearch_result['url'] = url_dict.get(str(geosearch_result['pageid']), "URL NOT FOUND")

    print(json.dumps(geosearch_results, indent=2))


if __name__ == '__main__':
    print_wikimedia_geosearch_results()
