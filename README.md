# xblstatus

[![Codacy Badge](https://www.codacy.com/project/badge/785595d972354a8ea08f8149ce40a5c5)](https://www.codacy.com/public/niklasjerva/xblstatus_2)

This tool is for checking Xbox Live status via a python script.
It can handle both consoles being affected and showing it properly.
I believe I've covered all possibility of 'limited' and 'up and running'. If you find an error or have code improvement do make a pull request.

~~Currently this only works locally. There will be a version which return all needed info Slack with formatting.~~

Now it works with Slack too.

If you want to use this in you Slack community create an outgoing webhook with the keyword '!xbl' and use http://xblstatus.herokuapp.com as the url.

![Screenshot](/static/xblstatus.png?raw=true "Screenshot")

#### TODO:
* ~~Make it Slack compatible~~ **Done**

* ~~Format the text properly for Slack~~ **Done**

* ~~Find a way to reduce IF-statements~~ ~~Only **2** IFs.~~ Multiple try-except phases...