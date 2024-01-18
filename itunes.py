import requests
import sys
import json

if len(sys.argv) != 2:
	print("Usage: python3 %s <url>" % sys.argv[0])
	sys.exit(1)

res = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=%s' % sys.argv[1])

print(json.dumps(res.json(), indent=4, sort_keys=True))

o = res.json()['results']

for r in o:
	print(r['trackName'])
