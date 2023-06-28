import requests

links = [{
  "url": "https://wttr.in/svo",
  "params": {
    "n": "",
    "m": "",
    "MTqu": "",
    "lang": "ru"
  }
}, {
  "url": "https://wttr.in/London",
  "params": {
    "n": "",
    "m": "",
    "MTqu": "",
    "lang": "ru"
  }
}, {
  "url": "https://wttr.in/Череповец",
  "params": {
    "n": "",
    "m": "",
    "MTqu": "",
    "lang": "ru"
  }
}]

for link in links:
  url, params = link["url"], link["params"]
  page = requests.get(url, params=params)
  print(page.text)
