# download gitenber db from apache dir after performing the istrctions here
# https://www.gutenberg.org/wiki/Gutenberg:Information_About_Robot_Access_to_our_Pages
import sys
import urllib
import re
import os

def list_apache_dir(url):
    try:
        html = urllib.urlopen(url).read()
    except IOError, e:
        print 'error fetching %s: %s' % (url, e)
        return
    if not url.endswith('/'):
        url += '/'
   
    dirs = re.findall(r'<img src=\"/icons/folder.gif\" alt=\"\[DIR\]\" width=\"12\" height=\"12\"> <a href=\"(\d+)\/">', html)
    text = re.findall(r'<img src=\"/icons/text.gif\" alt=\"\[TXT\]\" width=\"12\" height=\"12\"> <a href=\"(\d+\-?\d+.txt)\">',html)
    for d in dirs:
        list_apache_dir(url + d)
    for t in text:
       
        if not os.path.isfile('D:\Gutenberg/'+t):
            print url+t
            txt = urllib.urlretrieve(url+t, 'D:\Gutenberg/'+ t)
        else:
            print 'skipping ' +  url+t

url = 'http://www.gutenberg.lib.md.us/' 
list_apache_dir(url)
