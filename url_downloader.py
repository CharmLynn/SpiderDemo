# encoding:utf-8
import urllib2


class UrlDownlaoder(object):

    def dowload_url(self, url):
        if url is None :
            return None
        response = urllib2.urlopen(url)
        if response.code != 200:
            return None
        return response.read()
