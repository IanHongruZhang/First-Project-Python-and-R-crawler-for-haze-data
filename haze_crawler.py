#-*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
import random
import re
import time
import numpy

list_1 = []

class Wumai_Search():
    
    def execute(self,url):
        page_num = 1
        html = request.get(url,20)
        html.encoding = 'utf8'
        html_Soup = BeautifulSoup(html.text,'lxml')
        list_td = html_Soup.find("td",class_ = 'report1_5').find_all('font')
        max_num = list_td[1].get_text()
        while page_num <= int(20):
            url = 'http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=&startdate=2016-01-01&enddate=2017-01-01&page='+ str(page_num)
            self.read_html(url)
            page_num += 1
    
    def read_html(self,url):
        html = request.get(url, 20)
        html.encoding = 'utf8'
        html_Soup = BeautifulSoup(html.text,'lxml')
        list_td = html_Soup.find("table",{"id":"report1"}).find_all("td",{'class':'report1_9'})
        for li in list_td:
            print(li.get_text())
            k = li.get_text()
            list_1.append(k)

class download():
    def __init__(self):
        self.iplist = []  ##save the IP
        html = requests.get("http://haoip.cc/tiqu.htm")
        iplistn = re.findall(r'r/>(.*?)<b', html.text, re.S) ##get ID by RegEx 
            i = re.sub('\n', '', ip)  ##re.sub
            self.iplist.append(i.strip())  ##append id to a list
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
 
    def get(self, url, timeout, proxy = None, num_retries=2): ##default proxy == None
        print(u'开始获取：', url)
        UA = random.choice(self.user_agent_list) ##choose random header from self.user_agent_list
        headers = {'User-Agent': UA}  ##
        if proxy == None: ##
                return requests.get(url, headers=headers, timeout=timeout)##
                if num_retries > 0: ##
                    time.sleep(10) ##wait for 10s
                    print(u'获取网页出错，10S后将获取倒数第：', num_retries, u'次')
                    return self.get(url, timeout, num_retries-1)  
                else:
                    print(u'开始使用代理')
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    return self.get(url, timeout, proxy,) 

      
        else: 
            try:
                IP = ''.join(str(random.choice(self.iplist)).strip()) ##
                proxy = {'http': IP} 
                return requests.get(url, headers=headers, proxies=proxy, timeout=timeout) ##
                if num_retries > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http':IP}
                    print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                    print(u'当前代理是：', proxy)
                    return self.get(url, timeout, proxy, num_retries - 1)
                else:
                    print(u'代理也不好使了！取消代理')
                    return self.get(url, 20)
                
request = download()                
url = "http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=&startdate=2016-01-01&enddate=2017-01-01&page=1"
search = Wumai_Search()
#Hengyang.execute(url)
search.execute(url)