class UrlManager(object):

    def __init__(self):
        self.new_url_list = set()
        self.old_url_list = set()


    def add_new_url(self, root_url):
        if root_url is None :
            return
        if root_url not in self.old_url_list or root_url not in self.new_url_list:
            self.new_url_list.add(root_url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls)==0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_url_list)!=0


    def get_new_url(self):
        work_url = self.new_url_list.pop()
        self.old_url_list.add(work_url)
        return work_url

