import requests
from bs4 import BeautifulSoup
import cherrypy
import json

class xblStatus(object):
	exposed = True

	def GET(self):
		return json.dumps({'text': 'I\'m ALIVE!'})

	def POST(*args, **kwargs):
		r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
		soup = BeautifulSoup(r.content)
		g_data = soup.find_all("ul", {"class": "core"})
		status = {}

		for item in g_data:
			a = item.contents[1].find_all('h3')[1].text +' is ' + item.contents[1].find_all('span')[0].text
			try:
				if item.contents[1].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					if item.contents[1].find_all('p')[1].text == 'Xbox One' and item.contents[1].find_all('p')[2].text == 'Xbox 360':
						a = a + '. ' + 'Platforms: ' + item.contents[1].find_all('p')[1].text + ', ' + item.contents[1].find_all('p')[2].text
					else:
						a = a + '. ' +  'Platforms: ' + item.contents[1].find_all('p')[1].text
			except:
				pass
			print a

			b = '\n'+item.contents[3].find_all('h3')[1].text +' is ' + item.contents[3].find_all('span')[0].text
			try:
				if item.contents[3].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					if item.contents[3].find_all('p')[1].text == 'Xbox One' and item.contents[3].find_all('p')[2].text == 'Xbox 360':
						b = b + '. ' + 'Platforms: ' + item.contents[3].find_all('p')[1].text + ', ' + item.contents[3].find_all('p')[2].text
					else:
						b = b + '. ' +  'Platforms: ' + item.contents[3].find_all('p')[1].text
			except:
				pass
			print b

			c = '\n'+item.contents[5].find_all('h3')[1].text +' is ' + item.contents[5].find_all('span')[0].text
			try:
				if item.contents[5].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					if item.contents[5].find_all('p')[1].text == 'Xbox One' and item.contents[5].find_all('p')[2].text == 'Xbox 360':
						c = c + '. ' + 'Platforms: ' + item.contents[5].find_all('p')[1].text + ', ' + item.contents[5].find_all('p')[2].text
					else:
						c = c + '. ' +  'Platforms: ' + item.contents[5].find_all('p')[1].text
			except:
				pass
			print c

			d = '\n'+item.contents[7].find_all('h3')[1].text +' is ' + item.contents[7].find_all('span')[0].text
			try:
				if item.contents[7].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					if item.contents[7].find_all('p')[1].text == 'Xbox One' and item.contents[7].find_all('p')[2].text == 'Xbox 360':
						d = d + '. ' + 'Platforms: ' + item.contents[7].find_all('p')[1].text + ', ' + item.contents[7].find_all('p')[2].text
					else:
						d = d + '. ' +  'Platforms: ' + item.contents[7].find_all('p')[1].text
			except:
				pass
			print d

			e = '\n'+item.contents[9].find_all('h3')[1]. +' is ' + item.contents[9].find_all('span')[0].text
			try:
				if item.contents[9].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					if item.contents[9].find_all('p')[1].text == 'Xbox One' and item.contents[9].find_all('p')[2].text == 'Xbox 360':
						e = e + '. ' + 'Platforms: ' + item.contents[9].find_all('p')[1].text + ', ' + item.contents[9].find_all('p')[2].text
					else:
						e = e + '. ' +  'Platforms: ' + item.contents[9].find_all('p')[1].text
			except:
				pass
			print e

			return json.dumps({'text': '%s%s%s%s%s' % (a,b,c,d,e)})

# Start the Cherrypy server        
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(xblStatus(), '/', "app.conf")