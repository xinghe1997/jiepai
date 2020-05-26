import H
from lxml import etree
import os
import time
import requests
import threading
def getContent(url):
    #获取随机ip
    proxy = H.getProxys();
    content = H.getHtml(url,proxy)
    html = etree.HTML(content)
    #获取图片链接
    src = html.xpath("//div[@id='comments']/ul/li//p/img/@data-original")
    t = threading.Thread(target=downloadFile,args=(src,proxy,))
    t.start()
    t.join()
    #提取下一页连接
    page = html.xpath(" //a[@class='prev page-numbers']/@href")
    return str(page[0])
def downloadFile(src,proxy):
    jp = os.path.exists("D:\\BaiduNetdiskDownload\\街拍\\街拍图")
    if(jp):
        #改变目录
        os.chdir("D:\\BaiduNetdiskDownload\\街拍\\街拍图")
        for val in src:
            img = requests.get(str(val))
            name = str(int(time.time() * 10000))+os.path.splitext(val)[1]
            with open(name, 'wb') as f:
                f.write(img.content)
            f.close()
            
    else:
        os.mkdir('D:\\BaiduNetdiskDownload\\街拍\\街拍图')
        os.chdir("D:\\BaiduNetdiskDownload\\街拍\\街拍图")
        for val in src:
            img = requests.get(str(val))
            name = str(int(time.time() * 10000))+os.path.splitext(val)[1]
            with open(name, 'wb') as f:
                f.write(img.content)
            f.close()   
#继承threading,重写run方法
class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread,self).__init__()
    def run(self):
        url = "https://www.mzitu.com/jiepai/"
        page = getContent(url)
        #循环用户需要的页数
        for i in range(0,pageNum-1):
            page = getContent(page)
            
if __name__ == '__main__':
    page = ''
    pageNum = int(input("输入爬取的页数:"))
    if(pageNum > 1):
         #接收下一页
        stra = time.time()
        t = MyThread()
        t.start()
        print("运行时间为：",time.time() - stra)
    else:
        print(1)
        url = "https://www.mzitu.com/jiepai/"
        getContent(url)
   
