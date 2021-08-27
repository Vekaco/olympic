import scrapy


def get_flag_url(flag):
    start = flag.index("url(")
    end = flag.index(")")
    # should get after 'url('
    return flag[start + 4:end]


class CanaoBaiduSpider(scrapy.Spider):
    name = 'canao-baidu'
    allowed_domains = ['tiyu.baidu.com']
    start_urls = ['https://tiyu.baidu.com/tokyoly/paralympic/from/pc']

    def parse(self, response):
        rank = response.css('div[class="num"]>p::text').extract()
        flag = response.css('div[class="country-img"]>span[class="icon"]::attr(style)').extract()
        country = response.css('span[class="name"]::text').extract()
        gold = response.css('div[class*="item-gold"]::text').extract()
        silver = response.css('div[class*="item-silver"]::text').extract()
        bronze = response.css('div[class*="item-copper"]::text').extract()
        total = response.css('div[class*="item-all"]::text').extract()
        print(gold)
        idx = 0
        for temp in rank:
            yield {'rank': ''.join(rank[idx]),
                   'name': ''.join(country[idx]),
                   'flag': ''.join(get_flag_url(flag[idx])),
                   'gold': ''.join(gold[idx].replace('\n', '').strip()),
                   'silver': ''.join(silver[idx].replace('\n', '').strip()),
                   'bronze': ''.join(bronze[idx].replace('\n', '').strip()),
                   'total': ''.join(total[idx].replace('\n', '').strip())
                   }
            idx = idx + 1
        pass
