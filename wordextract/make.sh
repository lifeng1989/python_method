#! /bin/bash
if [ -z $1 ]
then 
	echo "usage:./make.sh 新词发现的文件"
	exit 1
fi
#修改数据把所有的字母转成C 所有的数字转成D
PATH_SORT=`which sort`
PATH_PYTHON=`which python`
CMD_PATH=`dirname $0`
mkdir m_$1
PATH=$CMD_PATH/m_$1
#下面有两个命令第一个是预处理普通文本，第二个是微店的标准存储数据
/usr/bin/awk '{gsub(/[A-Z,a-z]+/,"C",$0);gsub(/[0-9]+/,"D",$0);print $0}' $1 > $PATH/del_$1
#/usr/bin/awk '{gsub(/[A-Z,a-z]+/,"C",$0);gsub(/[0-9]+/,"D",$0);print $13}' $1 > $PATH/del_$1
#计算正序的字组合种类和数量
$PATH_PYTHON compute_candidate_freq.py -o $PATH/freq $PATH/del_$1
#计算逆序的字组合种类和数量
$PATH_PYTHON compute_candidate_freq.py -o $PATH/freq1 -r $PATH/del_$1
#计算字组合右边字的熵值
$PATH_PYTHON compute_freedegree.py -o $PATH/rfree $PATH/freq 
#计算字组合左边字的熵值
$PATH_PYTHON compute_freedegree.py -r -o $PATH/lfree $PATH/freq1
#计算字之间的结合紧密度
$PATH_PYTHON compute_solidation.py -o $PATH/solid $PATH/freq
#数据合并
cd m_$1
./../hebing.awk ../hebing.awk > alldata
cd ..
#整合参数
./cal.awk $PATH/alldata > $PATH/cal_alldata
#筛选数据
/usr/bin/awk '{if($1 > 0.95) print $0}' $PATH/cal_alldata > $PATH/choice_data
#新的排序规则(计算新的词判别算法)
/usr/bin/awk '{a = $4/(10*($5-$6)+1);a = (a>0? a:-a);print a"\t"$0}' $PATH/choice_data > $PATH/end_data
$PATH_SORT -g -k 1 -r -o $PATH/end_data $PATH/end_data
#跟字典去重的模块
#awk '{while (getline < "dict.txt") a[$1] = 1}{if(length($2) < 4&&a[$2] != 1) print $0}' end_data > end_del_data

