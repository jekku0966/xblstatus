import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
soup = BeautifulSoup(r.content)
g_data = soup.findAll('ul', {'class': 'core'})

for item in g_data:
	
	a = item.contents[1].find_all('h3')[0].text.split(item.contents[1].find_all('span')[0].text)[0] +' is ' + item.contents[1].find_all('span')[0].text
	try:
		if item.contents[1].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			if item.contents[1].find_all('p')[1].text == 'Xbox One' and item.contents[1].find_all('p')[2].text == 'Xbox 360':
				a = a + '. ' + 'Platforms: ' + item.contents[1].find_all('p')[1].text + ', ' + item.contents[1].find_all('p')[2].text
			else:
				a = a + '. ' +  'Platforms: ' + item.contents[1].find_all('p')[1].text
	except:
		pass
	print a

	b = '\n'+item.contents[3].find_all('h3')[0].text.split(item.contents[3].find_all('span')[0].text)[0] +' is ' + item.contents[3].find_all('span')[0].text
	try:
		if item.contents[3].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			if item.contents[3].find_all('p')[1].text == 'Xbox One' and item.contents[3].find_all('p')[2].text == 'Xbox 360':
				b = b + '. ' + 'Platforms: ' + item.contents[3].find_all('p')[1].text + ', ' + item.contents[3].find_all('p')[2].text
			else:
				b = b + '. ' +  'Platforms: ' + item.contents[3].find_all('p')[1].text
	except:
		pass
	print b

	c = '\n'+item.contents[5].find_all('h3')[0].text.split(item.contents[5].find_all('span')[0].text)[0] +' is ' + item.contents[5].find_all('span')[0].text
	try:
		if item.contents[5].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			if item.contents[5].find_all('p')[1].text == 'Xbox One' and item.contents[5].find_all('p')[2].text == 'Xbox 360':
				c = c + '. ' + 'Platforms: ' + item.contents[5].find_all('p')[1].text + ', ' + item.contents[5].find_all('p')[2].text
			else:
				c = c + '. ' +  'Platforms: ' + item.contents[5].find_all('p')[1].text
	except:
		pass
	print c

	d = '\n'+item.contents[7].find_all('h3')[0].text.split(item.contents[7].find_all('span')[0].text)[0] +' is ' + item.contents[7].find_all('span')[0].text
	try:
		if item.contents[7].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			if item.contents[7].find_all('p')[1].text == 'Xbox One' and item.contents[7].find_all('p')[2].text == 'Xbox 360':
				d = d + '. ' + 'Platforms: ' + item.contents[7].find_all('p')[1].text + ', ' + item.contents[7].find_all('p')[2].text
			else:
				d = d + '. ' +  'Platforms: ' + item.contents[7].find_all('p')[1].text
	except:
		pass
	print d

	e = '\n'+item.contents[9].find_all('h3')[0].text.split(item.contents[9].find_all('span')[0].text)[0] +' is ' + item.contents[9].find_all('span')[0].text
	try:
		if item.contents[9].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			if item.contents[9].find_all('p')[1].text == 'Xbox One' and item.contents[9].find_all('p')[2].text == 'Xbox 360':
				e = e + '. ' + 'Platforms: ' + item.contents[9].find_all('p')[1].text + ', ' + item.contents[9].find_all('p')[2].text
			else:
				e = e + '. ' +  'Platforms: ' + item.contents[9].find_all('p')[1].text
	except:
		pass
	print e