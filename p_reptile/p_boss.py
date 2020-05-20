# name -- 爬boss web前端开发工程师招聘要求
# 工具 -- selenium  https://pypi.tuna.tsinghua.edu.cn/simple清华大学下载镜像,这是一个zip文件~~和python解释器放在一起
# 查看python解释器，cmd里面where python，我放在scripts文件夹下面
# 目的 -- 简单学习selenium做爬虫或者自动化测试 https://npm.taobao.org/mirrors/chromedriver

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器
web = Chrome()
# 输入网页
web.get("https://www.lagou.com/")  #boss直聘遭遇502
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
# 找到输入框，输入“前端开发工程师”
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("web前端开发", Keys.ENTER)
time.sleep(1)
web.find_element_by_xpath('/html/body/div[8]/div/div[2]').click()
web.find_element_by_xpath('//*[@id="filterCollapse"]/div[1]/div[2]/li/div[2]/div/a[6]').click()
aList = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')
for a in aList:
    a.click()
    time.sleep(1)
    # 让浏览器打开一个新的窗口
    web.switch_to.window(web.window_handles[-1])
    job_desc = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text
    print(job_desc)
    print('====================================================================================')
    web.close()
    # 浏览器回到原来页面
    web.switch_to.window(web.window_handles[0])
    time.sleep(1)