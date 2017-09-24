import requests
import json

def synonym(word):
    #r = requests.get("https://wordsapiv1.p.mashape.com/words/care", headers={"X-Mashape-Key":"13O1LQlEtzmshTKI34ylotVawPVpp1c9sPPjsnTIU0cr5qURff"});
    r = requests.get("http://words.bighugelabs.com/api/2/9f827bcba258eac80d7a6451a23026af/" + word + "/json");
    print r
    json_data = json.loads(r.text)
    print json_data
    return json_data
