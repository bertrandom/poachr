#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import os, os.path

script_path = os.path.dirname(os.path.realpath(__file__))

response = urllib2.urlopen('http://www.flickr.com/about/')
html = response.read()

soup = BeautifulSoup(html)

buddyicons = soup.find('table').findAll('img')

names = []
nsids = []

for buddyicon in buddyicons:
	names.append(buddyicon["alt"])
	x = re.search('#(.*)', buddyicon["src"])
	nsids.append(x.group(1))

name_file = open(script_path + '/' + 'names.txt', 'w')

for name in names:
  name_file.write("%s\n" % name)

name_file.close()

nsid_file = open(script_path + '/' + 'nsids.txt', 'w')

for nsid in nsids:
  nsid_file.write("%s\n" % nsid)

nsid_file.close()