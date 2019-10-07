from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
import xlwt


browser = webdriver.Chrome()
browser.maximize_window()
#知识点
knowledgePoint = []
#题目数量
problemsNum = []
#分值占比
scorePercentage = []
#排名
rank = []
#错误率
wrongRate = []
#难度系数
hardDegree = []

def login():  #模拟登录
    url = 'http://www.rkpass.cn/tk_zhishidian.jsp?kemu_id=6&paper_id=0'
    browser.get(url)
    #time.sleep(2)
    browser.find_element_by_css_selector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td:nth-child(2) > a:nth-child(1) > span').click()
   # time.sleep(2)
    username= browser.find_element_by_id('username_1')
   # time.sleep(3)
    username.send_keys('785409363@qq.com')
    password = browser.find_element_by_id('password')
   # time.sleep(3)
    password.send_keys('123456')
   # time.sleep(2)
    browser.find_element_by_css_selector('body > table:nth-child(4) > tbody > tr > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td > div > div > div > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr:nth-child(7) > td:nth-child(2) > input[type=image]').click()


def getHtml():
    html = browser.find_element_by_xpath("//*").get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'lxml')
    return soup


def getKowledgePoint(soup):  #知识点
    text= soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(n) > td:nth-child(1) > a > span')
    for item in text:
        knowledgePoint.append(item.text)




def getQuantity(soup):  #题目数量（道）
    text = soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(n) > td:nth-child(2) > a > span')
    for item in text:
        problemsNum.append(item.text.strip())



def getPercent(soup): #分值占比
    text = soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(n) > td:nth-child(3)') #以下条目都去掉span
    for item in text:
        if item is not None:
            scorePercentage.append(item.text.strip())
        else:
            scorePercentage.append(" ")


def getRank(soup):  #排名
    text = soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(n) > td:nth-child(4)')
    for item in text:
        if item is not None:
            rank.append(item.text.strip())
        else:
            rank.append(" ")



def getWrongRate(soup):  #错误率
    text = soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(n) > td:nth-child(5)')
    for item in text:
        if item is not None:
            wrongRate.append(item.text.strip())
        else:
            wrongRate.append(" ")

def getDifficult(soup):  #难度系数
    text = soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(n) > td:nth-child(6)')
    for item in text:
        if item.find('img'):
            item1 = item.select('img')
            item2 = item1[0]
            link = item2.attrs['src']
            pattern = 'http://www.rkpass.cn/image/([1-9]+).gif'
            image = re.findall(pattern, link)
            rank = int(image[0]) - 50
            hardDegree.append(rank)  # 输出1-10的难度等级
        else:
            hardDegree.append(" ")



def save_excel():

    wb = xlwt.Workbook()
    ws = wb.add_sheet('软考爬虫',cell_overwrite_ok=True)
    list = ['知识点','题目数量(道)','分值占比','排名(名次)','错误率','难度系数']
    # 保存标题
    for i in range(0,len(list)):
        ws.write(0,i,list[i])

    totalLen = len(knowledgePoint)

    for i in range(1,totalLen+1):#行
        j = 2
        if scorePercentage[i]:
            ws.write(i,j,scorePercentage[i])   #2
        else:
            ws.write(i,j)
        j = j + 1
        if rank[i]:
            ws.write(i,j,rank[i])  #3
        else:
            ws.write(i,j)
        j = j + 1
        if wrongRate[i]:
            ws.write(i,j,wrongRate[i])  #4
        else:
            ws.write(i,j)

    for i in range(1,totalLen+1):
        ws.write(i,5,hardDegree[i])  #5



    #保存知识点
    for i in range(len(knowledgePoint)):
        ws.write(i+1,0,knowledgePoint[i])

    #保存题目数量
    for i in range(len(problemsNum)):
        ws.write(i+1,1,problemsNum[i])

    # #保存分值占比
    # for i in range(totalLen):
    #     if scorePercentage[i]:
    #         ws.write(i+1, 2, (scorePercentage[i]))
    #     else:
    #         ws.write(i+1,2," ")
    #
    #
    # # 保存排名
    # for i in range(totalLen):
    #     if rank[i]:
    #         ws.write(i+1, 3, (rank[i]))
    #     else:
    #         ws.write(i+1,3," ")
    #
    #
    # # 保存错误率
    # for i in range(totalLen):
    #     if wrongRate[i]:
    #         ws.write(i+1, 4, (wrongRate[i]))
    #     else:
    #         ws.write(i+1,4," ")
    #
    #
    # # 难度系数
    # for i in range(len(hardDegree)):
    #     if hardDegree[i]:
    #         ws.write(i + 1, 5, (hardDegree[i]))
    #     else:
    #         ws.write(i+1,5," ")


    wb.save('../Data/rkpass.xls')




if __name__ == '__main__':
    login()
    soup = getHtml()

    getKowledgePoint(soup)
    getQuantity(soup)
    getPercent(soup)
    getRank(soup)
    getWrongRate(soup)
    getDifficult(soup)
    save_excel()
    
