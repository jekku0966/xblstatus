import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status')
soup = BeautifulSoup(r.content, 'html5lib')
g_data = soup.findAll('ul', {'class': 'core'})

status = {}
# For testing purposes add these to status dictionary: 'lol': ['x1, 360, none'], 'test': ['teet, 111, XxX']


for item in g_data:

    for service in item.findAll('h3', {'class': 'servicename'}):
        status[service.text] = []
    for platform in item.findAll('div', {'class': 'label'}):
        status[service.text].append(platform.text)
    
for service,platform in status.items():
    if platform:
        platString = ''.join(platform)
        print('{} is limited. Platforms: {}'.format(service, platString))
    else:
        print('{} is up and running.'.format(service))