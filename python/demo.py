# -*- coding: UTF-8 -*-
# 用于检查需要爬取的信息能不能直接通过抓取网页源码得到
import ast

import requests
from bs4 import BeautifulSoup
import re
# 得到网页源码
def getText(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0',
            'Cookie': 'JSESSIONID=783339588E6EE142063AD2A47E35A344; Hm_lvt_7e54952498f03e835073b04894c29aa6=1569407178,1569424936,1569466325,1569481626; Hm_lpvt_7e54952498f03e835073b04894c29aa6=1569483009'
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '错误'


if __name__ == '__main__':
    url = "http://www.rkpass.cn/tk_zhishidian.jsp?kemu_id=6&paper_id=0"
    text = getText(url)
    soup = BeautifulSoup(text, 'lxml')
    spans = soup.find_all('span')
    print(spans)
    for tag in soup.find_all('div', class_='span'):
        print(tag)
        m_name = tag.find('span', class_='shisi_text_hui').get_text()
        print(m_name)
        #currentTable = tables[8]
 #   currentTable = tables[8]
 #    tables = soup.find_all('table')
 #    currentTable = tables[8]
 #
 #
 #    print(currentTable)

    # language = '<span class="shisi_text_hui">3.8%</span>'
    # res = '(?<= )class=".*?"'
    # match_class = currentTable(re.findall(res,language,re.S|re.M))
    # print(match_class)


# 爬取页面中的链接
# for link in soup.find_all('a'):
#     print(link.get('href'))
    #知识点和题目数量(道)
    # script = soup.find_all('script')
    # scriptStr = str(script)
    # start = scriptStr.find("data:")
    # end = scriptStr.find(']', start, start+600)
    # data = scriptStr[start+6:end].strip().replace('{', '').replace('}', '').split(',')
    # values = []
    # names = []
    # index = 1
    # for item in data:
    #     d = item.split(':')
    #     if index%2 == 0:
    #         names.append(d[1].replace('\'', ''))
    #     else:
    #         values.append(d[1])
    #     index += 1
    #
    # for item in names:
    #     print(item)
    # for item in values:
    #     print(item)
