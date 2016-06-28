#! /usr/bin/awk -f
{
#左熵
a = 3
#右熵
b = 3
#凝固度
c = 20000
if($3 > c && $4 > a && $5 > b)
		print $0
}
