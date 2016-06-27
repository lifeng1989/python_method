# _*_ coding: utf-8 _*_
import jieba
import time
#对输入的query进行分词处理
def searchQuery():
    a = []
    str1 = raw_input("请输入搜索语句：\n")
    for sstr in jieba.cut(str1):
        a.append(sstr)
    return a
def load():
    mydict = {}
    fp = open("data","r")
    for each in fp.readlines():
	each = each.replace('\n','')
	each = each.replace('\r','')
        a = each.split("\t")
        mydict[a[0]] = each
    fp.close()
    return mydict
	

#倒入数据,建立倒排索引(数据的格式第一列是id，其他列是商品描述切词后的词组)
def loadData():
    dict1 = {}
    fp = open("data","r")
    for each in fp.readlines():
        each = each.replace('\n','')
        each = each.replace('\r','')
        each = unicode(each,"utf-8")
        a = each.split("\t")
        for id in a[1:] :
            if id in dict1 :
                dict1[id].append(a[0])
            else :
                dict1[id]=[a[0]]
    for id in dict1:
        dict1[id] = list(set(dict1[id]))
	fp.close()
    return dict1
#这个是搜索策略一，搜索非常慢，放在这里做对比
'''
def itemSearch(query,bdict):
    flag = 1
    enddata = []
    alist = bdict.get(query[0],[])
    for id1 in alist:
        for id2 in query[1:]:
            if id1 not in bdict.get(id2,[]):
                flag = 0
                break
        if flag :
            enddata.append(id1)
        flag = 1
    return enddata

'''
#这个是搜索策略二、搜索的效果比上一个好上千倍
def itemSearch(query,bdict):
    enddata = []
    mydict1 = {}
    n = len(query)
    for id1 in query:
        for id2 in bdict.get(id1,[]):
            if mydict1.get(id2,0):
                mydict1[id2] += 1
            else :
                mydict1[id2] = 1
    for id in mydict1:
        if mydict1[id] == n:
            enddata.append(id)
    return enddata


if __name__ == "__main__":
    start = time.clock()
    mydict = loadData()
    mydict1 = load()
    elapsed = (time.clock() - start)
    print elapsed
    while True:
        myquery = searchQuery()
        start = time.clock()
        end=itemSearch(myquery,mydict)
        elapsed = (time.clock() - start)
        print "一共搜到%d条记录" % (len(end))
        print elapsed
	for id1 in end:
	    print mydict1[id1.encode("utf-8")]
