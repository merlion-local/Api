
# Weather Api <img style="border-radius: 50%;" width="300" style alt="Снимок экрана 2023-06-28 в 19 03 13" src="https://github.com/merlion-local/Api/assets/75911434/02f539f8-6da7-4166-a7ab-e1b2c5956ad4">


## Description
This script demonstrates how to use the `requests` library to fetch weather information from different URLs and print the resulting page content.


## Dependencies

- Python 3.x
- Requests library
- A little luck

You can install the `requests` library using pip
To install Requests, simply run this simple command in your terminal of choice:

```$ python3 -m pip install requests```





## Usage
Please make sure you have the requests library installed before running this script.

Open the terminal and go to the folder where the script is "weather.py " 

and then call ```$ python3 weather.py```



The following code snippet shows how to import the `requests` library and fetch data from the given URLs:



<p>https://wttr.in/svo?n?m?MTqu&lang=ru</p>
<p>https://wttr.in/London?n?m?MTqu&lang=ru</p>
<p>https://wttr.in/Череповец?n?m?MTqu&lang=ru</p>


This code iterates over the links list, makes a GET request using the requests.get() method, and prints the resulting page content.


```python
import requests

links = [
    {
        "url": "https://wttr.in/svo",
        "params": {"n": "", "m": "", "MTqu": "", "lang": "ru"}
    },
    {
        "url": "https://wttr.in/London",
        "params": {"n": "", "m": "", "MTqu": "", "lang": "ru"}
    },
    {
        "url": "https://wttr.in/Череповец",
        "params": {"n": "", "m": "", "MTqu": "", "lang": "ru"}
    }
]

for link in links:
    url, params = link["url"], link["params"]
    page = requests.get(url, params=params)
    print(page.text)
```
## The result of the script
Here is an actual weather report for your location (it's live!):

<img width="640" alt="Снимок экрана 2023-06-28 в 18 33 31" src="https://github.com/merlion-local/Api/assets/75911434/674541b9-e7fb-4134-a364-4630da0708a5">
<img width="637" alt="Снимок экрана 2023-06-28 в 18 33 54" src="https://github.com/merlion-local/Api/assets/75911434/90a0a60f-2b45-4345-955b-3462a9cbec07">
<img width="640" alt="Снимок экрана 2023-06-28 в 18 34 17" src="https://github.com/merlion-local/Api/assets/75911434/4b9f17e0-5e66-445a-98ab-5a7aeba2810b">


## Weather queries with parameters:
https://github.com/chubin/wttr.in
