import requests
from bs4 import BeautifulSoup
import cherrypy
import json

class xblStatus(object):
	exposed = True

	def GET(self):
		return json.dumps({'text': 'I\'m ALIVE!'})
		print 'I\'m ALIVE!'

	def POST(*args, **kwargs):
		r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
		soup = BeautifulSoup(r.content)
		g_data = soup.find_all("ul", {"class": "core"})
		status = {}
		plat = {}

		for item in g_data:
			status['tmv'] = item.contents[1].find_all('span')[0].text
			try:
				plat['tmv'] = item.contents[3].find_all('p')[1].text+', '+item.contents[3].find_all('p')[2].text
			except:
				pass
			try:
				plat['tmv'] = item.contents[1].find_all('p')[1].text
			except:
				pass
			status['cores'] = item.contents[3].find_all('span')[0].text
			try:
				plat['cores'] = item.contents[3].find_all('p')[1].text+', '+item.contents[3].find_all('p')[2].text
			except:
				pass
			try:
				plat['cores'] = item.contents[3].find_all('p')[1].text
			except:
				pass
			status['pc'] = item.contents[5].find_all('span')[0].text
			try:
				plat['pc'] = item.contents[5].find_all('p')[1].text+', '+item.contents[5].find_all('p')[2].text
			except:
				pass
			try:
				plat['pc'] = item.contents[5].find_all('p')[1].text
			except:
				pass
			status['site'] = item.contents[7].find_all('span')[0].text
			try:
				plat['site'] = item.contents[7].find_all('p')[1].text+', '+item.contents[7].find_all('p')[2].text
			except:
				pass
			try:
				plat['site'] = item.contents[7].find_all('p')[1].text
			except:
				pass
			status['sg'] = item.contents[9].find_all('span')[0].text
			try:
				plat['sg'] = item.contents[9].find_all('p')[1].text+', '+item.contents[9].find_all('p')[2].text
			except:
				pass
				try:
					plat['sg'] = item.contents[9].find_all('p')[1].text
				except:
					pass

		# All ok
		if bool(plat) == False:
			 return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], status['pc'], status['site'], status['sg'])})

		# Something is down
		if bool(plat) == True:
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], plat['tmv'], status['cores'], status['pc'], status['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], plat['cores'], status['pc'], status['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], status['pc'], plat['pc'], status['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], status['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], status['pc'], status['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], status['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], plat['tms'], status['cores'], status['pc'], plat['pc'], status['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], plat['tmv'], status['cores'], status['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], plat['tmv'], status['cores'], status['pc'], status['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], plat['cores'], status['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], plat['cires'], status['pc'], status['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], status['pc'], plat['pc'], status['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], status['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], plat['tmv'], status['cores'], status['cores'], status['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], plat['tmv'], status['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], status['sg'], plat['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'])})
			except:
				pass
			try:
				return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (status['tmv'], plat['tmv'], status['cores'], plat['cores'], status['pc'], plat['pc'], status['site'], plat['site'], status['sg'], plat['sg'])})
			except:
				pass

# Start the Cherrypy server        
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(xblStatus(), '/', "app.conf")
