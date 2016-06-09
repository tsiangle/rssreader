
import xmltodict
import urllib.request

class rssreader:
	def __init__(self):
		pass

	def getpage(url):
		return urllib.request.urlopen(url).read().decode()

	def xml2dict(xml):
		return xmltodict.parse(xml)

	def show(jstring):
		print(jstring)

rssreader.show(rssreader.xml2dict(rssreader.getpage("http://www.zhihu.com/rss")))
