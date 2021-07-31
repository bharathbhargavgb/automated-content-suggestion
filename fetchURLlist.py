from google import google
from xgoogle.search import GoogleSearch
num_page = 1

def findURLfromKeyword(keyword):
    search_results = google.search(keyword, num_page)
    URLs = []

    for result in search_results:
        if "wiki" in result.link:
            URLs.append(result.link)

    return URLs

def findURLfromKeyword_new(keyword):
    gs = GoogleSearch(keyword)
    gs.results_per_page = 10
    results = gs.get_results()
    for res in results:
        print res.title.encode('utf8')

findURLfromKeyword_new("artificial intelligence")
