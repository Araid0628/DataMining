from scrapy import Selector
import urllib.request
import pandas as pd

def getURL():                #抓取工程院院士的URL和姓名
    page = urllib.request.urlopen('http://www.cae.cn/cae/html/main/col48/column_48_1.html')
    html = page.read()
    urlList = []
    sel = Selector(text=html, type="html")
    urlList = sel.xpath('//li[re:test(@class, "name_list")]//@href').extract()
    nameList = sel.xpath('//li[re:test(@class, "name_list")]//a/text()').extract()
    #print(url)
    i = 0
    for i in range(len(urlList)):
        urlList[i] = "http://www.cae.cn" + urlList[i]
    return urlList, nameList
    #print(url)


def getInfo(academyURL):     #抓取院士的具体信息
    infoPage = urllib.request.urlopen(academyURL)
    infoHTML = infoPage.read()
    infoSelect = Selector(text=infoHTML, type="html")
    info = infoSelect.xpath('//div[@class="intro"]/p/text()').extract()[0]
    return info

def main():                 #main()
    urlList, nameList = getURL()
    infoList = []
    for i in range(len(urlList)):
        infoList.append(getInfo(urlList[i]))
    print(len(infoList), len(nameList))
    filepath = r"E:\nlp\week2\abc.csv"
    dataframe = pd.DataFrame({'姓名':nameList, '简介':infoList})
    dataframe.to_csv(filepath, encoding='utf_8_sig')

if __name__ == "__main__":
    main()






