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
			a = item.contents[1].find_all('h3')[0].text.split(item.contents[1].find_all('span')[0].text)[0] +' is ' + item.contents[1].find_all('span')[0].text
			try:
				if item.contents[1].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					try:
						a = a + '. ' + 'Platforms: ' + item.contents[1].find_all('p')[1:2].text
					except:
						a = a + '. ' +  'Platforms: ' + item.contents[1].find_all('p')[1].text
			except:
				pass
				a = a


			b = '\n'+item.contents[3].find_all('h3')[0].text.split(item.contents[3].find_all('span')[0].text)[0] +' is ' + item.contents[3].find_all('span')[0].text
			try:
				if item.contents[3].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					try:
						b = b + '. ' +  'Platforms: ' + item.contents[3].find_all('p')[1:2].text
					except:
						b = b + '. ' +  'Platforms: ' + item.contents[3].find_all('p')[1].text
			except:
				pass
				b = b

			c = '\n'+item.contents[5].find_all('h3')[0].text.split(item.contents[5].find_all('span')[0].text)[0] +' is ' + item.contents[5].find_all('span')[0].text
			try:
				if item.contents[5].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					try:
						c = c + '. ' +  'Platforms: ' + item.contents[5].find_all('p')[1:2].text
					except:
						c = c + '. ' +  'Platforms: ' + item.contents[5].find_all('p')[1].text
			except:
				pass
				sc = c

			d = '\n'+item.contents[7].find_all('h3')[0].text.split(item.contents[7].find_all('span')[0].text)[0] +' is ' + item.contents[7].find_all('span')[0].text
			try:
				if item.contents[7].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					try:
						d = d + '. ' +  'Platforms: ' + item.contents[7].find_all('p')[1:2].text
					except:
						d = d + '. ' +  'Platforms: ' + item.contents[7].find_all('p')[1].text
			except:
				pass
				d = d

			e = '\n'+item.contents[9].find_all('h3')[0].text.split(item.contents[9].find_all('span')[0].text)[0] +' is ' + item.contents[9].find_all('span')[0].text
			try:
				if item.contents[9].find_all('span', {'class': 'unavailable'})[0].text == 'Limited':
					try:
						e = e + '. ' +  'Platforms: ' + item.contents[9].find_all('p')[1:2].text
					except:
						e = e + '. ' +  'Platforms: ' + item.contents[9].find_all('p')[1].text
						pass
			except:
				pass
				e = e

			return json.dumps({'text': '%s%s%s%s%s' % (a,b,c,d,e)})

# Start the Cherrypy server        
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(xblStatus(), '/', "app.conf")