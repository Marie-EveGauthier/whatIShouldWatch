import scrapy
import csv

def geturls():
    with open('movieinfo.csv') as csvfile:
        reader = csv.reader(csvfile)
        movieinfo = list(reader) #stores characters, words spoken

    movieinfoforurls = movieinfo[0:5]
    print '\n movieinfo ', movieinfo[0], '\n'
    movieurls = ['http://www.imdb.com/title/' + movie[-1] + '/fullcredits?ref_=tt_ov_st_sm' for movie in movieinfoforurls]
    print movieurls

    return movieurls


class QuotesSpider(scrapy.Spider):
    name = "getcrewurls"
    start_urls = geturls()

    def parse(self, response):
        for person in response.css('td.name'):
            yield {
                person.xpath('a/text()').extract_first():person.xpath('a/@href').extract_first(),
                #'movie': response.xpath('//title/text()'), # <- this breaks it for some reason
                #'name': person.xpath('a/text()').extract_first(), #person.css('a::text').extract_first(),
                #'url': person.xpath('a/@href').extract_first(), # person.css('a').extract_first(),
            }


"""
Trying to get just the writers and directors (doesnt work):
        #table = response.xpath(("//h4[contains(text(), 'Directed')]/following-sibling::table[1]")
        #for person in table.css('td.name'):

        for i in response.xpath('//h4[contains(text(), 'Directed')]'):
        #for i in nodes.xpath('dt'):
        #print i.xpath('a/text()').extract()
            yield { i.xpath('following-sibling::table[1]text()').extract() }


        #yield {
        #    'table': response.xpath(("//h4[contains(text(), 'Directed')]/following-sibling::table[1]"),
        #}

    start_urls = [
        'http://www.imdb.com/title/tt0066921/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt1939659/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0114938/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0081383/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0070355/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt1204977/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0490076/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0190590/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0083967/fullcredits?ref_=tt_ov_st_sm',
        'http://www.imdb.com/title/tt0488120/fullcredits?ref_=tt_ov_st_sm',
    ]


"""
