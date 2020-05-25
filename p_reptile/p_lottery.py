import requests
from lxml import etree   #分析数据



# 抓取彩票数据
resp = requests.get('') # 新加坡暂时访问不了www.500.com 提取network网址
# print(resp.text)
# we should put all of html info into etree
hm = etree.HTML(resp.text)
# search the tbody tr what the id is tdata from HTML
trs = hm.xpath("//tbody[@id='tdata']/tr")
for tr in trs:
    data_lst = tr.xpath('td/text()')
    m = map(lambda x: x.replace(',', '').replace('\xa0', ''), data_lst)
    s = ','.join(m)
    f.write(s + '\n')
    # 写入文件 data.csv文件
