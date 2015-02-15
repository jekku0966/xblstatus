import requests
from bs4 import BeautifulSoup
import cherrypy
import json

class xblStatus(object):
	exposed = True

	def GET(self):
		return json.dumps({'text': 'I\'m ALIVE!'})

	def POST(*arg, **kwargs):
		r = requests.get('http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
		soup = BeautifulSoup(r.content)
		g_data = soup.find_all("ul", {"class": "core"})
		music_plat = None
		cores_plat = None
		content_plat = None
		site_plat = None
		social_plat = None

		for item in g_data:
			# TV, Music and Video
			music = item.contents[1].find_all('span')[0].text
		try:
			item.contents[1].find_all('span', {'class': 'unavailable'})[0].text
			music_plat = item.contents[1].find_all('p')[1].text
		except:
			pass
			#Xbox Live Core Services
		cores = item.contents[3].find_all('span')[0].text
		try:
			item.contents[3].find_all('span', {'class': 'unavailable'})[0].text
			cores_plat = item.contents[3].find_all('p')[1].text
		except:
			pass
			# Purchase and Content Usage
		content = item.contents[5].find_all('span')[0].text
		try:
			item.contents[5].find_all('span', {'class': 'unavailable'})[0].text
			content_plat = item.contents[5].find_all('p')[1].text
		except:
			pass
			# Website
		site = item.contents[7].find_all('span')[0].text
		try:
			item.contents[7].find_all('span', {'class': 'unavailable'})[0].text
			site_plat = item.contents[7].find_all('p')[1].text
		except:
			pass
			# Social and Gaming
		social = item.contents[9].find_all('span')[0].text
		try:
			item.contents[9].find_all('span', {'class': 'unavailable'})[0].text
			social_plat = item.contents[9].find_all('p')[1].text
		except:
			pass

		# All is ok
		if music_plat == None and cores_plat == None and content_plat == None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (music, cores, content, site, social)})

		# All is not ok
		if music_plat != None and cores_plat != None and content_plat != None and site_plat != None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (music, music_plat, cores, cores_plat, content, content_plat, site, site_plat, social, social_plat)})

		# Music down, others ok
		if music_plat != None and cores_plat == None and content_plat == None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (music, music_plat, cores, content, site, social)})

		# Core services down, others ok
		if music_plat == None and cores_plat != None and content_plat == None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (music, cores, cores_plat, content, site, social)})

		# Purchase&Content down, others ok
		if music_plat == None and cores_plat == None and content_plat != None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (music, cores, content, content_plat, site, social)})

		# Website down, others ok
		if music_plat == None and cores_plat == None and content_plat == None and site_plat != None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (music, cores, content, site, site_plat, social)})

		# Social&Gaming down, others ok
		if music_plat == None and cores_plat == None and content_plat == None and site_plat == None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (music, cores, content, site, social, social_plat)})

		# Music and Core services down, others ok
		if music_plat != None and cores_plat != None and content_plat == None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s' % (music, music_plat, cores, cores_plat, content, site, social)})

		# Music and P&C down, others ok
		if music_plat != None and cores_plat == None and content_plat != None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (music, music_plat, cores, content, content_plat, site, social)})

		# Music and Website down, others ok
		if music_plat != None and cores_plat == None and content_plat == None and site_plat != None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (music, music_plat, cores, content, site, site_plat, social)})

		# Music and S&G down, others ok
		if music_plat != None and cores_plat == None and content_plat == None and site_plat == None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (music, music_plat, cores, content, site, social, social_plat)})

		# Cores services and P&C down, others ok
		if music_plat == None and cores_plat != None and content_plat != None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (music, cores, cores_plat, content, content_plat, site, social)})

		# Core services and Website down, others ok
		if music_plat == None and cores_plat != None and content_plat == None and site_plat != None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (music, cores, cores_plat, content, site, site_plat, social)})

		# Core services and S&G down, others ok
		if music_plat == None and cores_plat != None and content_plat == None and site_plat == None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (music, cores, cores_plat, content, site, social, social_plat)})

		#  P&C and Website down, others ok
		if music_plat == None and cores_plat == None and content_plat != None and site_plat != None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platfoem: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (music, cores, content, content_plat, site, site_plat, social)})

		# P&C and social down, others ok
		if music_plat == None and cores_plat == None and content_plat != None and site_plat == None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s, Platform: %s' % (music, cores, content, content_plat, site, social, social_plat)})

		# Website and S&G down, others ok
		if music_plat == None and cores_plat == None and content_plat == None and site_plat != None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (music, cores, content, site, site_plate, social, social_plat)})

		#	Music, Core services and P&G down, others ok
		if music_plat != None and cores_plat != None and content_plat != None and site_plat == None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s\nSocial and Gaming is %s' % (music, music_plat, cores, cores_plat, content, content_plat, site, social)})

		# Music, P&C and Website down, others ok
		if music_plat != None and cores_plat == None and content_plat != None and site_plat != None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (music, music_plat, cores, content, content_plat, site, site_plat, social)})

		if music_plat != None and cores_plat == None and content_plat == None and site_plat != None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s, Platform: %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (music, music_plat, cores, content, site, site_plat, social, social_plat)})

		# Core services, P&C and Website down, others ok
		if music_plat == None and cores_plat != None and content_plat != None and site_plat != None and social_plat == None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s' % (music, cores, cores_plat, content, content_plat, site, site_plat, social)})

		# Core services, Website and S&G down, others ok
		if music_plat == None and cores_plat != None and content_plat == None and site_plat != None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s, Platform: %s\nPurchase and Content Usage is %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (music, cores, cores_plat, content, site, site_plat, social, social_plat)})

		# P&G, Webiste and S&G down, others ok
		if music_plat == None and cores_plat == None and content_plat != None and site_plat != None and social_plat != None:
			return json.dumps({'text': 'TV, Music and Video is %s\nXbox Live Core Services is %s\nPurchase and Content Usage is %s, Platform: %s\nWebsite is %s, Platform: %s\nSocial and Gaming is %s, Platform: %s' % (music, cores, content, content_plat, site, site_plat, social, social_plat)})


# Start the Cherypy server        
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(xblStatus(), '/', "app.conf")