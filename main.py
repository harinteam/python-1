import requests

"""
print("Hello World!")
r = requests.get('http://harinteam.com')
print(r.status_code)
if r.status_code == 200:
    print(r.text)
"""

try :
    r = requests.get('https://www.goo gle.co.id')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Ada error', e)