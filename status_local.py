import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')

soup = BeautifulSoup(r.content)

g_data = soup.find_all("ul", {"class": "core"})

for item in g_data:
	print 'TV, Music and Video is ' + item.contents[1].find_all('span')[0].text
	try:
		item.contents[1].find_all('span', {'class': 'unavailable'})[0].text
		print 'Affected platforms: ' + item.contents[1].find_all('p')[1].text
	except:
		pass
	print ''
	print 'Xbox Live Core Services is ' + item.contents[3].find_all('span')[0].text
	try:
		item.contents[3].find_all('span', {'class': 'unavailable'})[0].text
		print 'Affected platforms: ' + item.contents[3].find_all('p')[1].text
	except:
		pass
	print ''
	print 'Purchase and Content Usage is ' + item.contents[5].find_all('span')[0].text
	try:
		item.contents[5].find_all('span', {'class': 'unavailable'})[0].text
		print 'Affected platforms: ' + item.contents[5].find_all('p')[1].text
	except:
		pass
	print ''
	print 'Website is ' + item.contents[7].find_all('span')[0].text
	try:
		item.contents[7].find_all('span', {'class': 'unavailable'})[0].text
		print 'Affected platforms: ' + item.contents[7].find_all('p')[1].text
	except:
		pass
	print ''
	print 'Social and Gaming is ' + item.contents[9].find_all('span')[0].text
	try:
		item.contents[9].find_all('span', {'class': 'unavailable'})[0].text
		print 'Affected platforms: ' + item.contents[9].find_all('p')[1].text
	except:
		pass