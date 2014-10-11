import re

class MagnetFinder:
	def __init__ (self):
		self.full_link_pattern = re.compile('magnet:\?xt=urn:btih:[0-9a-z]*&dn=.*&tr=[a-zA-Z0-9%.]*')
		self.grouped_link_pattern = re.compile('(magnet:\?){1}(xt=urn:btih:){1}([0-9a-z]*){1}(&dn=.*){1}(&tr=[a-zA-Z0-9%.]*)+')
		
	def get_magnet_links (self,raw_html, magnet_terminator):
		selection=re.findall(self.full_link_pattern,raw_html)
		return selection
