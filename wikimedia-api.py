import json

import requests

# Documentation
# How to search by location : https://commons.wikimedia.org/wiki/Commons:Search_by_location
# Geosearch query : https://www.mediawiki.org/wiki/Extension:GeoData#list=geosearch

WIKIMEDIA_BASE_URL = "https://commons.wikimedia.org/w/api.php?"

SEARCH_RADIUS_METERS = 500  # Distance around the coordinate we search
SEARCH_COORDINATES = '49.0222493192745|2.000689441938519'  # Coordinates around which we search, in lat|long format
NUMBER_SEARCH_RESULT = 10  # Max 500 per search


def search_wikimedia_image_with_url() -> None:
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

    pretty_print_json(wikimedia_response.text)


def search_Wikimedia_file_only() -> None:
    wikimedia_response = requests.get(f'{WIKIMEDIA_BASE_URL}'
                                      'action=query&'
                                      'format=json&'
                                      f'gscoord={SEARCH_COORDINATES}&'
                                      'gsnamespace=6&'  # Namespace 6 is the file namespace in wikimedia
                                      'gsprimary=all&'
                                      f'gsradius={SEARCH_RADIUS_METERS}&'
                                      f'gslimit={NUMBER_SEARCH_RESULT}&'
                                      'list=geosearch')

    pretty_print_json(wikimedia_response.text)


def pretty_print_json(json_string: str) -> None:
    json_parsed = json.loads(json_string)
    print(json.dumps(json_parsed, indent=2))


if __name__ == '__main__':
    search_wikimedia_image_with_url()
