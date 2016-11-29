import requests
import json

events_type_file = open('event_types.txt', 'w')
url = "http://push.cricbuzz.com/match-api/16870/commentary.json"
response = requests.get(url)
data = json.loads(response.text)
comm_lines = data["comm_lines"]
events = set()
for line in comm_lines:
    print line
    events.add(line["evt"])
for item in events:
    events_type_file.write(item + "\n")
    events_type_file.flush()
