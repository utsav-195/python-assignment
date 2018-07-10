import json
from pprint import pprint

with open('dataS3.json') as f:
    data = json.load(f)

pprint(data)
