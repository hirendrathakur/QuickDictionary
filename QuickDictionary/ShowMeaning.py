import gtk
from Dictionary import Dictionary
class ShowMeaning():
	def __init__(self):
		self.start_process()

	def start_process(self):
		clipboard = gtk.clipboard_get()
		last_text = clipboard.wait_for_text()
		while(True):
			current_text = clipboard.wait_for_text()
			if str.isalpha(current_text) and current_text!=last_text:
				print "Copied %s..." %current_text
				Dictionary(current_text)
			last_text = current_text