import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
soup = BeautifulSoup(r.content)
g_data = soup.find_all("ul", {"class": "core"})
status = {}
plat = {}

for item in g_data:

        status['tmv']= item.contents[1].find_all('span')[0].text
        try:
                plat['tmv'] = item.contents[1].find_all('p')[1].text+', '+item.contents[1].find_all('p')[2].text
        except:
                pass

        if bool(plat) == False:
                try:
                        plat['tmv'] = item.contents[1].find_all('p')[1].text
                except:
                        pass


        status['cores'] = item.contents[3].find_all('span')[0].text
        try:
                plat['cores'] = item.contents[3].find_all('p')[1].text+', '+item.contents[3].find_all('p')[2].text
        except:
                pass

        if bool(plat) == False:
                try:
                        plat['cores'] = item.contents[3].find_all('p')[1].text
                except:
                        pass

        status['pc'] = item.contents[5].find_all('span')[0].text
        try:
                plat['pc'] = item.contents[5].find_all('p')[1].text+', '+item.contents[5].find_all('p')[2].text
        except:
                pass
        if bool(plat) == False:
                try:
                        plat['pc'] = item.contents[5].find_all('p')[1].text
                except:
                        pass

        status['site'] = item.contents[7].find_all('span')[0].text
        try:
                plat['site'] = item.contents[7].find_all('p')[1].text+', '+item.contents[7].find_all('p')[2].text
        except:
                pass
        if bool(plat) == False:
                try:
                        plat['site'] = item.contents[7].find_all('p')[1].text
                except:
                        pass

        status['sg'] = item.contents[9].find_all('span')[0].text
        try:
                plat['sg'] = item.contents[9].find_all('p')[1].text+', '+item.contents[9].find_all('p')[2].text
        except:
                pass
        if bool(plat) == False:
                try:
                        plat['sg'] = item.contents[9].find_all('p')[1].text
                except:
                        pass


print 'TV, Music and Video is ' + status['tmv']
try:
	print 'Affected platforms: ' + plat['tmv']
except:
	pass
print '\nXbox Live Core Services is ' + status['cores']
try:
	print 'Affected platforms: ' + plat['cores']
except:
	pass
print '\nPurchase and Content Usage is ' + status['pc']
try:
	print 'Affected platforms: ' + plat['pc']
except:
	pass
print '\nWebsite is ' + status['site']
try:
	print 'Affected platforms: ' + plat['site']
except:
	pass
print '\nSocial and Gaming is ' + status['sg']
try:
	print 'Affected platforms: ' + plat['sg']
except:
	pass
