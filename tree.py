import urllib
from xml.etree.ElementTree import ElementTree

rss = ElementTree()
rss.parse("rss.xml")

ElementTree.dump(rss)

