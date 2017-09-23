from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBcH4x8fSFs6t-v7aEVoiey3M4oBYK_lzQ"
my_cse_id = "005831625243409643462:lk59bvjjssa"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'artificial intelligence wikipedia', my_api_key, my_cse_id, num=10)
for result in results:
    print result['link']
