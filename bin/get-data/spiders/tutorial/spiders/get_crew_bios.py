import scrapy
import csv
import re

def geturls():
    with open('writer_noentry_imdburls.csv') as csvfile:
        reader = csv.reader(csvfile)
        urllist = list(reader) #stores characters, words spoken

    #print '\n movieinfo ', movieinfo[0], '\n'
    urls = [entry[1] for entry in urllist]
    #print movieurls

    return urls


class bioSpider(scrapy.Spider):
    name = "getcrewbios"
    start_urls = geturls()

    def parse(self, response):
        name = response.xpath('//h1/span/text()').extract_first()
        bio = response.css('div.inline::text').extract_first()
        #bio = re.sub("<(.+?)>(.+?)</.+?)>", " ", bio_with_links)
        yield {
            'name': name,
            'bio': bio,
        }
