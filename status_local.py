import requests
from bs4 import BeautifulSoup

r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
soup = BeautifulSoup(r.content)
g_data = soup.findAll('ul', {'class': 'core'})

for item in g_data:
	
	a = item.contents[1].find_all('h3')[0].text.split(item.contents[1].find_all('span')[0].text)[0] +' is ' + item.contents[1].find_all('span')[0].text
	try:
		if item.contents[1].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			try:
				a = a + '. ' + 'Platforms: ' + item.contents[1].find_all('p')[1:2].text
				print a
			except:
				a = a + '. ' +  'Platforms: ' + item.contents[1].find_all('p')[1].text
				print a
	except:
		pass
		print a

	b = '\n'+item.contents[3].find_all('h3')[0].text.split(item.contents[3].find_all('span')[0].text)[0] +' is ' + item.contents[3].find_all('span')[0].text
	try:
		if item.contents[3].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			try:
				b = b + '. ' +  'Platforms: ' + item.contents[3].find_all('p')[1:2].text
				print b
			except:
				b = b + '. ' +  'Platforms: ' + item.contents[3].find_all('p')[1].text
				print b
				pass
	except:
		pass
		print b

	c = '\n'+item.contents[5].find_all('h3')[0].text.split(item.contents[5].find_all('span')[0].text)[0] +' is ' + item.contents[5].find_all('span')[0].text
	try:
		if item.contents[5].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			try:
				c = c + '. ' +  'Platforms: ' + item.contents[5].find_all('p')[1:2].text
				print c
			except:
				c = c + '. ' +  'Platforms: ' + item.contents[5].find_all('p')[1].text
				print c
	except:
		pass
		print c

	d = '\n'+item.contents[7].find_all('h3')[0].text.split(item.contents[7].find_all('span')[0].text)[0] +' is ' + item.contents[7].find_all('span')[0].text
	try:
		if item.contents[7].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			try:
				d = d + '. ' +  'Platforms: ' + item.contents[7].find_all('p')[1:2].text
				print d
			except:
				d = d + '. ' +  'Platforms: ' + item.contents[7].find_all('p')[1].text
				print d
				pass
	except:
		pass
		print d

	e = '\n'+item.contents[9].find_all('h3')[0].text.split(item.contents[9].find_all('span')[0].text)[0] +' is ' + item.contents[9].find_all('span')[0].text
	try:
		if item.contents[9].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
			try:
				e = e + '. ' +  'Platforms: ' + item.contents[9].find_all('p')[1:2].text
				print e
			except:
				e = e + '. ' +  'Platforms: ' + item.contents[9].find_all('p')[1].text
				print e
				pass
	except:
		pass
		print e