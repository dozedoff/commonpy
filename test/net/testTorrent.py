import unittest

import commonpy.net.torrent as torrent

class TestTorrent (unittest.TestCase):
	html = '<a href="magnet:?xt=urn:btih:33d04dc722d17a405519d7c5ee022e1c0f957da1&dn=LinuxonAndroid+Project+Ubuntu+12.04+Core+Image&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337" title="Download this torrent using magnet"><img src="/static/img/icon-magnet.gif" alt="Magnet link" /></a>			<a href="//piratebaytorrents.info/7150593/LinuxonAndroid_Project_Ubuntu_12.04_Core_Image.7150593.TPB.torrent" title="Download this torrent"><img src="/static/img/dl.gif" class="dl" alt="Download" /></a><img src="/static/img/11x11p.png" /><img src="/static/img/11x11p.png" />'
	html2 = """<div class="detName">			<a href="/torrent/5522247/Ubuntu_10.04_LTS_Lucid_Lynx_Desktop_vmware_image" class="detLink" title="Details for Ubuntu 10.04 LTS Lucid Lynx Desktop vmware image">Ubuntu 10.04 LTS Lucid Lynx Desktop vmware image</a>
</div>
<a href="magnet:?xt=urn:btih:5fc8fdef02b0628a4d6115a048c9090069fd5977&dn=Ubuntu+10.04+LTS+Lucid+Lynx+Desktop+vmware+image&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337" title="Download this torrent using magnet"><img src="/static/img/icon-magnet.gif" alt="Magnet link" /></a>			<a href="//piratebaytorrents.info/5522247/Ubuntu_10.04_LTS_Lucid_Lynx_Desktop_vmware_image.5522247.TPB.torrent" title="Download this torrent"><img src="/static/img/dl.gif" class="dl" alt="Download" /></a><img src="/static/img/icon_comment.gif" alt="This torrent has 2 comments." title="This torrent has 2 comments." /><img src="/static/img/11x11p.png" />
			<font class="detDesc">Uploaded 04-30&nbsp;2010, Size 1.08&nbsp;GiB, ULed by <a class="detDesc" href="/user/bitbkk/" title="Browse bitbkk">bitbkk</a></font>
		</td>
		<td align="right">0</td>
		<td align="right">1</td>
	</tr>
	<tr>
		<td class="vertTh">
			<center>
				<a href="/browse/300" title="More from this category">Applications</a><br />
				(<a href="/browse/303" title="More from this category">UNIX</a>)
			</center>
		</td>
		<td>
<div class="detName">			<a href="/torrent/8410169/Ubuntu_GNOME_13.04_Raring_Ringtail_Desktop_image_for_64-bit_PC_(" class="detLink" title="Details for Ubuntu GNOME 13.04 Raring Ringtail Desktop image for 64-bit PC (">Ubuntu GNOME 13.04 Raring Ringtail Desktop image for 64-bit PC (</a>
</div>
<a href="magnet:?xt=urn:btih:36be2135abccf4032fbb28bb1b0d4fdaf749f858&dn=Ubuntu+GNOME+13.04+Raring+Ringtail+Desktop+image+for+64-bit+PC+%28&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337" title="Download this torrent using magnet"><img src="/static/img/icon-magnet.gif" alt="Magnet link" /></a>			<a href="//piratebaytorrents.info/8410169/Ubuntu_GNOME_13.04_Raring_Ringtail_Desktop_image_for_64-bit_PC_(.8410169.TPB.torrent" title="Download this torrent"><img src="/static/img/dl.gif" class="dl" alt="Download" /></a><img src="/static/img/11x11p.png" /><img src="/static/img/11x11p.png" />
			<font class="detDesc">Uploaded 04-25&nbsp;2013, Size 942&nbsp;MiB, ULed by <a class="detDesc" href="/user/linux_rox/" title="Browse linux_rox">linux_rox</a></font>
		</td>
		<td align="right">3</td>
		<td align="right">0</td>
	</tr>
	<tr>
"""
	magnet = 'magnet:?xt=urn:btih:33d04dc722d17a405519d7c5ee022e1c0f957da1&dn=LinuxonAndroid+Project+Ubuntu+12.04+Core+Image&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337'
	magnet2 = 'magnet:?xt=urn:btih:5fc8fdef02b0628a4d6115a048c9090069fd5977&dn=Ubuntu+10.04+LTS+Lucid+Lynx+Desktop+vmware+image&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337'
	magnet3 = 'magnet:?xt=urn:btih:36be2135abccf4032fbb28bb1b0d4fdaf749f858&dn=Ubuntu+GNOME+13.04+Raring+Ringtail+Desktop+image+for+64-bit+PC+%28&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337'
	
	def setUp (self):
		self.magnet_finder = torrent.MagnetFinder()

	def test_get_magnet_links_content_dep (self):
		found =  self.magnet_finder.get_magnet_links(self.html, "1337")
		self.assertEqual(found[0], self.magnet)

	def test_get_magnet_links_count_dep (self):
		found =  self.magnet_finder.get_magnet_links(self.html, "1337")
		self.assertEqual(len(found), 1)

	def test_get_magnet_links_content2_dep (self):
		found =  self.magnet_finder.get_magnet_links(self.html2, "1337")
		self.assertEqual(found[0], self.magnet2)
		self.assertEqual(found[1], self.magnet3)

	def test_get_magnet_links_count2_dep (self):
		found =  self.magnet_finder.get_magnet_links(self.html2, "1337")
		self.assertEqual(len(found), 2)
	
	def test_get_magnet_links_content (self):
		found =  self.magnet_finder.get_magnet_links(self.html)
		self.assertEqual(found[0], self.magnet)

	def test_get_magnet_links_count (self):
		found =  self.magnet_finder.get_magnet_links(self.html)
		self.assertEqual(len(found), 1)

	def test_get_magnet_links_content2 (self):
		found =  self.magnet_finder.get_magnet_links(self.html2)
		self.assertEqual(found[0], self.magnet2)
		self.assertEqual(found[1], self.magnet3)

	def test_get_magnet_links_count2 (self):
		found =  self.magnet_finder.get_magnet_links(self.html2)
		self.assertEqual(len(found), 2)
		
	def test_get_magnet_tuples_count (self):
		found = self.magnet_finder.get_magnet_tuples(self.html2)
		self.assertEqual(len(found), 2)
		
	def test_get_magnet_tuples_hash (self):
		found = self.magnet_finder.get_magnet_tuples(self.html2)
		self.assertEqual(found[0][0], "5fc8fdef02b0628a4d6115a048c9090069fd5977")
		
	def test_get_magnet_tuples_magnet (self):
		found = self.magnet_finder.get_magnet_tuples(self.html2)
		self.assertEqual(found[0][1], "magnet:?xt=urn:btih:5fc8fdef02b0628a4d6115a048c9090069fd5977&dn=Ubuntu+10.04+LTS+Lucid+Lynx+Desktop+vmware+image&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337")
		
	def test_get_magnet_tuples_name (self):
		found = self.magnet_finder.get_magnet_tuples(self.html2)
		self.assertEqual(found[0][2], "Ubuntu+10.04+LTS+Lucid+Lynx+Desktop+vmware+image")
