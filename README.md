# 这个工程是我学习python过程中自己写的一些小项目

## 搜索引擎

> 这个程序中用到的数据是我在微店实习的时候的商品数据，通过简单的倒排索引存储，利用jieba分词进行切词后在倒排索引表中查找商品，找到各个list的相同商品然后输出

#####使用方法

1. git clone 项目
2. cd search
3. python search.py 或者 python search1.py

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
4. 文档中的search1和search的区别只在于数据样式，search只输出id，search1输出整条数据
## 简单计算器

> 这是利用逆波兰表达式，做的简易的基于堆栈的计算器，只支持加减乘除和小括号，数据都是转成浮点数统一运算，目前没有加入运算式的错误检查

#####使用方法

cd cal
python cal.py

#####输入输出

输入:运算式 例如：2.2*(45+32)/190等

输出: 运算结果

## 螺旋数字输出

> 这是2016年腾讯的一个机试题，考的是如何对矩阵螺旋式的访问

#####使用方法

cd snake 

python snake.py

#####输入输出

输入：一个正整数 例如:5
输出：一个数字的螺旋矩阵：

1	2	3	4	5
16	17	18	19	6
15	24	25	20	7
14	23	22	21	8
13	12	11	10	9

##知乎爬虫

> 这是为了爬取知乎的问题和关注这个问题的人的数据集

######使用方法

cd crawler

python crawler1.py 或者 python crawler.py

######输入输出

输入：需要手动修改知乎需要爬去的url段，和浏览器的Cookie

输出： all.txt 是错误的没有数据的url content.txt 是爬取下来的数据

######输出数据样式

id | 内容
-- | ---
21049115 | 和喜欢的女孩子不知道说什么怎么办？
xue-xiao-shan-85 | 雪小禅
wang-zhao-yang-2-16 | 王昭仰


1. 第一行是问题，包括两个字段，分别是唯一标志符和问题
2. 第二行往后是关注这个问题的用户，也包含两个字段，分别是用户id和用户名


**注意**

1. crawler.py 是只爬问题，crawler是两个都爬
2. 使用前需要利用浏览器的开发者工具填写Cookie，使用crawler.py 的话忽略这个问题
