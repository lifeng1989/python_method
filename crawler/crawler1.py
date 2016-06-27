#-*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys
import socket
import gzip
import urllib2
import StringIO
reload(sys)

sys.setdefaultencoding('gbk')

#获取网数据
def getHtml(url):
    #头信息需要自己根据浏览器开发者工具中的的信息填写
    req_header={}
    try:
        req = urllib2.Request(url,None,req_header)
        page = urllib2.urlopen(req,timeout=10)
        data = page.read()
        #爬取的网页时压缩gzip格式所以要先解压
	compressedStream = StringIO.StringIO(data)
        gzipper = gzip.GzipFile(fileobj=compressedStream)
        data = gzipper.read()
    except socket.timeout, e:
        data = None
        print >>f1,"time out!"
    except urllib2.URLError,ee:
        data = None
        print >>f1,"%s error" %(url)
    finally:
        return data

#解析网页数据
def spider(url):
    html = getHtml(url)
    if(html != None):
        url1 = url+"/followers"
	html1 = getHtml(url1)
        selector = etree.HTML(html)
        content_field = selector.xpath('//*[@id="zh-question-title"]/h2/span/text()')
        for each in content_field:
           each = each.decode('gbk').encode('utf-8')
           print >> f,"%s\t%s" %(url.split("/")[-1],each)
        if (html1 != None):
             selector1 = etree.HTML(html1)
             content_field = selector1.xpath('//*[@id="zh-question-followers-list-wrap"]/div[*]/div[2]/h2/a/text()')
             content_field1 = selector1.xpath('//*[@id="zh-question-followers-list-wrap"]/div[*]/div[2]/h2/a/@data-tip')
             mylist = []
             mylist1 = []
             for each in content_field1:
                 each = each.split("$")[-1]
                 mylist.append(each)
	     for each in content_field:
                 each = each.decode('gbk').encode('utf-8')
		 mylist1.append(each)
             for i,j in zip(mylist,mylist1):
                 print >> f,"%s\t%s" %(i,j)
        print >> f,"###########################################################"

		 
if __name__ == '__main__':
    pool = ThreadPool(1)
    f = open('content.txt','w')
    f1 = open('all.txt','w')
    page = []
    for i in range(21049100,21049200):
        newpage = 'https://www.zhihu.com/question/'+str(i)
        page.append(newpage)
	
    results = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()
