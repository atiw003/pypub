#!/usr/bin/env python
# encoding: utf-8
"""
Snappy documentation goes here
@author: Heather Piwowar
@contact:  hpiwowar@gmail.com
@status:  playing around
"""

import sys
import os
import nose
from nose.tools import assert_equals
from tests import slow, online, notimplemented, acceptance
import dataset
import datasources
from datasources import highwire
from utils.cache import TimedCache

if __name__ == '__main__':
    nose.runmodule()
    
def get_this_dir():
    module = sys.modules[__name__]
    this_dir = os.path.dirname(os.path.abspath(module.__file__))
    return(this_dir)
        
# Shared test data
gold_first_filename = os.path.join(get_this_dir(), 'testdata', 'highwire_gold_results.html')
gold_first_page = open(gold_first_filename, "r").read()
gold_first_citations = ['Cancer Res.|2007|67|5117||test', 'J. Immunol.|2007|178|7097||test', 'J. Immunol.|2007|178|5154||test', 'Mol. Cell. Biol.|2007|27|1868||test', 'J. Immunol.|2007|179|557||test']

class TestHighwire(object):
    def test_get_citations_from_page(self):
        items_dict = highwire.get_citations_from_page(gold_first_page)
        lookup_lines = highwire.convert_items_to_lookup_strings(items_dict)
        assert_equals(lookup_lines[0:5], gold_first_citations)
    
    def test_get_citation_file_from_pages_in_directory(self):
        glob_pattern = os.path.join(get_this_dir(), 'testdata', 'highwire', "*", "*.html")
        list_of_citation_strings = highwire.get_citations_from_directories(glob_pattern, "highwire;")
        for str in list_of_citation_strings[0:10]:
            print str
        assert_equals(len(list_of_citation_strings), 639)
        assert_equals(list_of_citation_strings[0:5], ['J. Biol. Chem.|2007|282|13854||highwire;predef_all', 'J. Immunol.|2007|178|5154||highwire;predef_all', 'Blood|2007|109|1202||highwire;predef_all', 'J. Biol. Chem.|2007|282|32935||highwire;predef_all', 'Mol. Cell. Biol.|2007|27|4058||highwire;predef_all'])
        
        
    