import pynotify
import urllib
from bs4 import BeautifulSoup

class Dictionary():
	def __init__(self, word):
		self.word = word
		self.get_url(word)
	
	def get_url(self, word):
		self.base_url = 'http://google-dictionary.so8848.com/meaning?word='
		self.url = self.base_url+str(word)
		self.get_meaning()
	
	def get_meaning(self):
		html_obj = urllib.urlopen(self.url)
		html_string = html_obj.read().decode('utf-8')
		#parser.feed(html_string)
		bs_obj = BeautifulSoup(html_string,"lxml")
		content = bs_obj.find_all('li')
		#content = bs_obj.find_all('div',attrs = {"class":"std"})
		if pynotify.init('Basic'):
			result = content[4].contents[0]
			n = pynotify.Notification("Instant Dictionary: \n%s" %self.word,"Meaning for: %s\n%s" %(self.word, result))
			n.set_urgency(pynotify.URGENCY_NORMAL)
			n.set_timeout(200)
			n.show()