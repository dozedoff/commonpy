import re

def get_magnet_links (raw_html, magnet_terminator):
	regex_query = "magnet:\?xt=.*%s" % (magnet_terminator)
	selection=re.findall(regex_query,raw_html)
	return selection
