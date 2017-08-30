class ResultOutputer(object):
    def __init__(self):
        self.data = []
    def collect_data(self, new_data):
        if new_data is None:
            return None
        self.data.append(new_data)

    def out_put_data(self):
        fout = open("spider.html","w")
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for mydata in self.data:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % mydata['url'])
            fout.write('<td>%s</td>' % mydata['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % mydata['summry'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')


        fout.close()

