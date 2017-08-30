import urlparse

from bs4 import BeautifulSoup
import re

class ContentParser(object):

    def parse_content(self, url,http_cont):
        if url is None or http_cont is None:
            return None
        soup  = BeautifulSoup(http_cont,"html.parser",from_encoding='utf-8')
        newurls = self._get_new_url(url,soup)
        newdata = self._get_new_data(url,soup)
        return newurls,newdata

    def _get_new_url(self, url, soup):

        new_urls = set()
        links =  soup.find_all('a',target="_blank",href=re.compile(r"/item/.+"))
        for link in links:
            new_url  = link['href']
            new_full_url = urlparse.urljoin(url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        new_data = {}
        new_data['url'] = url
        title_link = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = title_link.get_text()
        summry_link = soup.find('div',class_='lemma-summary')
        new_data['summry'] = summry_link.get_text()
        return  new_data
