#! /usr/bin/python
import url_manager
import url_downloader
import content_parser
import result_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = url_downloader.UrlDownlaoder()
        self.parser = content_parser.ContentParser()
        self.outputer = result_outputer.ResultOutputer()

    def crawl(self,root_url):
        self.urls.add_new_url(root_url)
        count =1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "crawling %s,and url is %s" % (count,new_url)
                http_cont = self.downloader.dowload_url(new_url)
                new_urls,new_data = self.parser.parse_content(new_url,http_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                count = count +1
                if count == 100:
                    break
            except:
                print "crawl failed"
        self.outputer.out_put_data()
if __name__ == '__main__':
    root_url ="https://baike.baidu.com/item/Python"
    object_spider = SpiderMain()
    object_spider.crawl(root_url)