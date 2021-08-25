import scrapy


class MedalSpider(scrapy.Spider):
    name = 'medal'
    allowed_domains = ['olympics.com']
    start_urls = ['https://olympics.com/tokyo-2020/paralympic-games/en/results/all-sports/medal-standings.htm']

    def parse(self, response):
        table = response.css('table')
        rank = table.css('td[class="text-center"] > strong::text').extract()
        country = table.css('td >div > a[class="country"]::text').extract()
        flag = table.css('td >div > a[class="country"]>img[class="flag"]::attr(src)').extract()
        gold = table.css('td[class="text-center"] > a[title*="Gold"]::text').extract()
        silver = table.css('td[class="text-center"] > a[title*="Silver"]::text').extract()
        bronze = table.css('td[class="text-center"] > a[title*="Bronze"]::text').extract()
        total = table.css('td[class="text-center"] > a[title*="Total"]> strong::text').extract()
        i = 0
        for temp in rank:
            yield {'rank': ''.join(rank[i]),
                   'country': ''.join(country[i]),
                   'flag': ''.join(flag[i].replace('../../..', 'https://olympics.com/tokyo-2020/paralympic-games')),
                   'gold': ''.join(gold[i].replace('\r', '')),
                   'silver': ''.join(silver[i].replace('\r', '')),
                   'bronze': ''.join(bronze[i].replace('\r', '')),
                   'total': ''.join(total[i].replace('\r', ''))

                   }
            i = i+1
        pass
