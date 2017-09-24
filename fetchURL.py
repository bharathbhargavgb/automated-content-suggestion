#THE BELOW CODE WORKS FINE BUT THE API ALLOWS ONLY 100  REQUESTS PER DAY

#from googleapiclient.discovery import build
#import pprint

#my_api_key = "AIzaSyAqqRFrZLDceW7othVvstkQ5cxaTmV_rXE"
#my_cse_id = "005831625243409643462:vawfilusxna"

#results = []

#def google_search(search_term, api_key, cse_id, **kwargs):
#    service = build("customsearch", "v1", developerKey=api_key)
#    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#    return res['items']
#
#def findURLfromKeyword(keyword):
#    results = google_search(keyword, my_api_key, my_cse_id, num=10)
#    URLs = []
#    for result in results:
#        if result['link'] not in URLs:
#            URLs.append(result['link'])
#    return URLs#

from bs4 import BeautifulSoup
import requests
#import re

#regex = re.compile(
#        r'^(?:http|ftp)s?://' # http:// or https://
#        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
#        r'localhost|' #localhost...
#        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
#        r'(?::\d+)?' # optional port
#        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def findURLfromKeyword(keyword):
    url = []
    r  = requests.get("https://www.google.co.in/search?q=" + keyword)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    for field in soup.find_all("cite"):
        if 'en.wikipedia.org' in field.text and "..." not in field.text:
            url.append(field.text)            
    return url

findURLfromKeyword("hello")
