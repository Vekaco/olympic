# Description
crawl Tokyo2020 Paralympic medal count and generate csv report

# 概述
爬取东京残奥会奖牌榜信息，整理成csv格式

##How to run?
```angular2html
cd /olympic

scrapy runspider canao/canao/spiders/medal.py -o ./output/report.csv
```
## 如何运行？
```angular2html
cd /olympic

scrapy runspider canao/canao/spiders/medal.py -o ./output/report.csv
```

##Where is the report?
it depends on the -o options you input,
as the above params, the report file is generated on /olympic/output/report.csv

##生成的报表在哪里？
这取决于你运行时设定的 -o 参数，
如上面的命令运行，那么报表应该在/olympic/output/report.csv

##What can you do for the csv file?
I use this file for wechat mini program page rendering.
wechat scan to see more:
![image](https://vekaco.fun/10.jpg)

##csv报表能做什么？
我用它来生成微信小程序的页面
微信扫一扫：
![image](https://vekaco.fun/10.jpg)
