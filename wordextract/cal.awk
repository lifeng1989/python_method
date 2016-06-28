#! /usr/bin/awk -f
BEGIN{
	#凝固度
	a1 = 5000
	a2 = 1.9
	#频率
	b1 = 60
	b2 = 2
	#自由度
	c1 = 1.2
	c2 = 0
}
{
	if ($2 > b1)
			a = 1
	else if($2 < b2)
			a = 0
	else
			a = ($2 - b2)/(b1-b2)
	if($3 > a1)
			b = 1
	else if($3 < a2)
			b = 0
	else 
			b = ($3 - a2)/(a1-a2)
	if($4 > c1)
			c = 1
	else if($4 < c2)
			c = 0
	else 
			c = ($4 - c2)/(c1-c2)
	if($5 > c1)
			d = 1
	else if($5 < c2)
			d = 0
	else 
			d = ($5 - c2)/(c1-c2)
	print (a+b+c+d)/4"\t"$0
}