import re

class MagnetFinder:
	def __init__ (self):
		self.full_link_pattern = re.compile('magnet:\?xt=urn:btih:[0-9a-zA-Z]*&dn=.*&tr=[a-zA-Z0-9%.:/]*')
		self.grouped_link_pattern = re.compile('((magnet:\?)(xt=urn:btih:)([0-9a-zA-Z]*)(&dn=.*)(&tr=[a-zA-Z0-9%.:/]*)+)')
		
	# Deprecated = (self,raw_html, magnet_terminator)
	def get_magnet_links (self,raw_html, magnet_terminator = None):
		selection=re.findall(self.full_link_pattern,raw_html)
		return selection

	def get_magnet_tuples (self, html):
		tupels = []

		iter = re.finditer(self.grouped_link_pattern, html)
		
		for match in iter:
			set = (match.group(4), match.group(0))
			tupels.append(set)
		
		return tupels
