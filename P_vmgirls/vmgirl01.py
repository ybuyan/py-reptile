import requests
import re
import os

# 反爬header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}

# 用requests获取网址内容
response = requests.get('https://www.vmgirls.com/9384.html', headers=headers)
html = response.text;
# 正则获取图片链接
urls = re.findall('<img alt=".*?" src=".*?" data-src="(.*?)" data-nclazyload="true">', html)

# 生成图片文件夹
title = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0]
dir_name = 'vmimg/' + title
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# 下载保存图片
for url in urls:
    # time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    # with open as f 语句读写文件夹  IO操作
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)

