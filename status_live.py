import requests
from bs4 import BeautifulSoup
import cherrypy
import json


class xblStatus(object):
    exposed = True

    def GET(self):
        return json.dumps({'text': 'I\'m ALIVE!'})

    def POST(*args, **kwargs):
        r = requests.get(
            'http://support.xbox.com/en-US/xbox-live-status?icid=furl_status')
        soup = BeautifulSoup(r.content, 'html5lib')
        g_data = soup.find_all("ul", {"class": "core"})
        status = {}

        for item in g_data:
            for service in item.findAll('h3', {'class': 'servicename'}):
                status[service.text] = []
            for platform in item.findAll('div', {'class': 'label'}):
                status[service.text].append(platform.text)
        outputOk = []
        outputDown = []
        for service, platform in status.items():
            if platform:
                platString = ''.join(platform)
                outputDown.append(
                    '{} is limited. Platforms: {}\n'.format(service, platString))
            else:
                outputOk.append('{} is up and running.\n'.format(service))
            strOk = ''.join(outputOk)
            strDown = ''.join(outputDown)
        if strDown and strOk:
            return json.dumps({'attachments': [{'fallback': strOk, 'title': 'These systems are online:', 'text': strOk, 'color': '#008000'}, {'fallback': strDown, 'title': 'These systems are down:', 'text': strDown, 'color': '#FF0000'}]})
        elif strDown and not strOk:
            return json.dumps({'attachments': [	{'fallback': strDown, 'title': 'These systems are down:', 'text': strDown, 'color': '#FF0000'}]})
        else:
            return json.dumps({'attachments': [{'fallback': strOk, 'title': 'These systems are online:', 'text': strOk, 'color': '#008000'}]})


# Start the Cherrypy server
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(xblStatus(), '/', "app.conf")
