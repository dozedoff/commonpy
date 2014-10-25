import sys
import os
import re
from subprocess import check_output
from subprocess import call
import subprocess as subprocess

extent_pattern = re.compile('(: )([0-9]*)( extents? found)')

def walk_directory (root_path):
	file_paths = []
	for root_path, dir, files in os.walk(root_path):
		for items in files:
			fullpath="%s/%s" % (root_path,items)
			file_paths.append(fullpath)

	return file_paths

def get_extents (file_path):
	output=check_output(["filefrag", file_path],stderr=subprocess.STDOUT, bufsize=-1)
	return _regex_extent_count(output)

def _regex_extent_count (output):
	iter = re.finditer(extent_pattern, output)

	for match in iter:
		extents=match.group(2)
		return int(extents)
	
	return -1

def btrfs_defragment (file_path):
	call(["btrfs", "fi" ,"defrag", "-f", "-t", "10g",file_path])
