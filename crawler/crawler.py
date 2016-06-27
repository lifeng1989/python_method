#-*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys
import socket
import gzip
import urllib2
reload(sys)

sys.setdefaultencoding('gbk')

def getHtml(url):
#    data = None
    try:
        page = urllib2.urlopen(url,timeout=10)
        data = page.read()
    except socket.timeout, e:
        data = None
        print >>f1,"time out!"
        with open("timeout",'a') as log:
            log.write(url+'\n')
    except urllib2.URLError,ee:
        data = None
        print >>f1,"%s error" %(url)
    finally:
        return data

def spider(url):
    html = getHtml(url)
    if(html != None):
        selector = etree.HTML(html)
#        title = selector.xpath('//*[@id="name"]/h1/text()')
        content_field = selector.xpath('//*[@id="zh-question-title"]/h2/span/text()')
#        f.writelines(title+'\n')
        for each in content_field:
           each = each.decode('gbk').encode('utf-8')
           print >> f,"%s\t%s" %(url.split("/")[-1],each)
#            f.writelines(each)
#        f.writelines("###########################################################\n")
#        f1.writelines(html+'\n')
if __name__ == '__main__':
    pool = ThreadPool(1)
    f = open('content.txt','w')
    f1 = open('all.txt','w')
    page = []
    for i in range(21049150,21049160):
        newpage = 'https://www.zhihu.com/question/'+str(i)
#        spider(newpage)
        page.append(newpage)
	
    results = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()
