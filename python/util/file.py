import sys
import os
import re
from subprocess import check_output
from subprocess import call

def walk_directory (root_path):
	file_paths = []
	for root_path, dir, files in os.walk(root_path):
		for items in files:
			fullpath="%s/%s" % (root_path,items)
			file_paths.append(fullpath)

	return file_paths

def get_extents (file_path):
	output=check_output(["filefrag", file_path])
	selection=re.findall(": [0-9]* extents? found",output)
	selection=re.findall("[0-9]*",selection[0])
	extents=int(selection[2])
	return extents

def btrfs_defragment (file_path):
	call(["btrfs", "fi" ,"defrag", "-t", "10g",file_path])
