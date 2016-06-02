# 这个工程是我学习python过程中自己写的一些小项目

## 搜索引擎

> 这个程序中用到的数据是我在微店实习的时候的商品数据，通过简单的倒排索引存储，利用jieba分词进行切词后在倒排索引表中查找商品，找到各个list的相同商品然后输出

#####使用方法

1. git clone 项目
2. cd search
3. python search.py

#####输入输出

输入: 你的产训query
输出: 商品id列表

#####运行效果

我在我的mac（8g内存，2.7G）上测试140W条商品（140M数据），建立倒排需要17s , 搜索耗时都毫秒级

#####数据组织格式

taobao10000001223	特价	壁纸	/	客厅	壁纸	/	卧室	墙纸	【	简欧	压花	纸	基	胶	面	壁纸

1. 第一列是商品的id
2. 从第二列开始往后都是商品描述切词后的产出的词
3. 中间都是用\t分割

**注意**

1. 程序中依赖的jieba分词可以直接通过 sudo pip install jieba 安装
2. python 版本要求2.7及以上
3. 数据我只放了10W条作为测试用

## 项目二