import unittest

import commonpy.util.file as uf

class TestFile (unittest.TestCase):
    def test__regex_extent_count_multiple (self):
        extents = uf._regex_extent_count("foo.bar: 42 extents found")
        self.assertEqual(extents, 42)
        
    def test__regex_extent_count_single (self):
        extents = uf._regex_extent_count("foo.bar: 1 extent found")
        self.assertEqual(extents, 1)
        
    def test__regex_extent_count_not_found_error (self):
        extents = uf._regex_extent_count("open: No such file or directory")
        self.assertEqual(extents, 1)

    def test__regex_extent_count_file_access_error (self):
        extents = uf._regex_extent_count("open: Permission denied")
        self.assertEqual(extents, 1)
