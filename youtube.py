import urllib
import urllib2
from bs4 import BeautifulSoup
import sys

flag = 0
textToSearch = 'hello world'
query = sys.argv[1].strip("\"").replace(" ","+")
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,"lxml")
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
    	flag = 1
    	print 'https://www.youtube.com' + vid['href']
if flag == 0:
	print "No results found"