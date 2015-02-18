import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
soup = BeautifulSoup(r.content)
g_data = soup.find_all("ul", {"class": "core"})
status = {}
plat = {}

for item in g_data:
        for service in item.find_all('li'):
                service = service.h3.text[:-14]
                status[service] = []
                for platform in item.find_all('ul', {'class': 'platform'}):
                        status[service].append(platform.find('p').text)

output = []
for service, platforms in status.items():
        if platforms:
                line = '{} is limited. Platforms {}'
        else:
                line = '{} is up and running'
        output.append(line.format(service, ', '.join(platforms)))

print '\n'.join(output)