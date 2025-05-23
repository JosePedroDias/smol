import os

import requests
from dotenv import load_dotenv

load_dotenv()

"""WIP"""

CONF_PAT = os.getenv("CONF_PAT")
BASE_URL = "https://wiki.at.sky"

headers = {
    "Authorization": f"Bearer {CONF_PAT}"
}

# https://docs.atlassian.com/atlassian-confluence/REST/6.6.0/#content-search

def search_confluence(query):
    url = f"{BASE_URL}/rest/api/content/search"
    params = {
        "cql": f"text ~ \"{query}\"",
        "limit": 5,
        "expand": "body.view"
    }
    response = requests.get(
        url,
        params=params,
        headers={
            'Accept': 'application/json',
            **headers,
        }
    )
    print(response.status_code)
    print(response.headers.get("Content-Type"))
    #response.raise_for_status()
    return response.json()

def confluence_page_contents(search_results):
    pages = []
    for result in search_results.get('results', []):
        title = result['title']
        html_content = result['body']['view']['value']
        pages.append({"title": title, "html": html_content})
    return pages

def page_data(page_id):
    url = f"{BASE_URL}/rest/api/content/{page_id}"
    response = requests.get(
        url,
        headers={
            'Accept': 'application/json',
            **headers,
        }
    )
    print(response.status_code)
    print(response.headers.get("Content-Type"))
    #response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    #results = search_confluence('champ')
    #print(results)
    
    print(page_data("1016364635"))
