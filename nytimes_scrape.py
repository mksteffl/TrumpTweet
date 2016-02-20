import json, requests
import re

url = 'http://api.nytimes.com/svc/topstories/v1/politics.json?api-key=56ba07f49c4fe92ecb2624d7baab30ed:10:74482807'

resp = requests.get(url=url)
data = resp.json()
results = data['results']

out_file = open("times.txt", "wt")
for result in results:
    out_file.write(result['abstract'].encode('utf8') + '\n')
out_file.close()
