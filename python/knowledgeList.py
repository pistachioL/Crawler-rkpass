import requests
from bs4 import BeautifulSoup
import bs4
#body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(1) > span
#body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > span

    def getHTMLText(url):
        try:
            r = requests.get(url)
            r.rase_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return "出错!"

    def getKnowledgeList(list,url):
        return ""

    def getKnowledgeInfo(list,url,fpath):
        return ""


    def main():
        url = "http://www.rkpass.cn/tk_zhishidian.jsp"
        output_file = "/home/liao/Document/Python/RK_knowledgeList.txt"
        slist = []
        getKnowledgeList(slist,url)
        getKnowledgeInfo(slist,url,output_file)


main()