"""
This spider should get a list of character names for the filme
"""


import scrapy
import csv
from bs4 import BeautifulSoup

def geturls():
    with open('movieinfo.csv') as csvfile:
        reader = csv.reader(csvfile)
        movieinfo = list(reader) #stores characters, words spoken

    movieinfoforurls = movieinfo[:5]
    print '\n movieinfo ', movieinfo[0], '\n'
    movieurls = ['http://www.imdb.com/title/' + movie[-1] + '/fullcredits?ref_=tt_ov_st_sm' for movie in movieinfoforurls]
    print movieurls

    return movieurls


class charSpider(scrapy.Spider):
    name = "getcharnames"
    start_urls = geturls()

    def parse(self, response):
        characters = []
        for character in response.xpath('.//td[@class="character"]/div').extract():
            soup = BeautifulSoup(character)
            text = soup.get_text()
            text = text.replace('\n', ' ')
            text = text.strip()
            characters.append(text)
        yield {
            'movie': response.css('title::text').extract_first(),
            'characters': characters,
            }


### NEED TO EXTRACT DIFFERENTLY IS THE DIV CONTAINS A LINK OR NOT!!!!            for character in response.xpath('//td[@class="character"]/div/a/text()').extract()
