import requests


links=["https://wttr.in/svo?n?m?MT?&lang=ru&","https://wttr.in/London?n?m?MT&lang=ru","https://wttr.in/череповец?n?m?MT&lang=ru"]
for url in links:
    page = requests.get(url)
    print(page.text)





