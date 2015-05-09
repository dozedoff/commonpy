import requests

def get_page (url):
    page = requests.get(url)
    return page.text