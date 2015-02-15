import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')

soup = BeautifulSoup(r.content)

g_data = soup.find_all("ul", {"class": "core"})

for item in g_data:
	print 'TV, Music and Video ' + item.contents[1].find_all('span')[0].text
	try:
		if item.contents[1].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			print 'Affected platforms: ' + item.contents[1].find_all('p')[1].text
	except:
		pass
		print ''
		print 'Xbox Live Core Services ' + item.contents[3].find_all('span')[0].text
	try:
		if item.contents[3].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			print 'Affected platforms: ' + item.contents[3].find_all('p')[1].text
	except:
		pass
		print ''
		print 'Purchase and Content Usage ' + item.contents[5].find_all('span')[0].text
	try:
			if item.contents[5].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
				print 'Affected platforms: ' + item.contents[5].find_all('p')[1].text
	except:
		pass
		print ''
		print 'Website ' + item.contents[7].find_all('span')[0].text
	try:
		if item.contents[7].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			print 'Affected platforms: ' + item.contents[7].find_all('p')[1].text
	except:
		pass
		print ''
		print 'Social and Gaming ' + item.contents[9].find_all('span')[0].text
	try:
		if item.contents[9].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			print 'Affected platforms: ' + item.contents[9].find_all('p')[1].text
	except:
		pass