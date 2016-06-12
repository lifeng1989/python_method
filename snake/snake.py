# _*_ coding: utf-8 _*_
#ore是用来控制方向的
ore = ((0,1),(1,0),(0,-1),(-1,0))
try :
	i = int(raw_input("输入矩阵的大小:\n"))
except :
	print "错误出入，输入一个正整数"
	exit()
#初始化一个二维数组
mylist = [(["0"]*i) for k in range(i)]
j = 1
x = 0
y = 0
k = 0
while j <= i*i:
	#这个是赋值并往前走
	if(x >= 0 and x < i and y >=0 and y < i and mylist[x][y] == "0"):
		mylist[x][y] = str(j)
		j = j+1
		x = x + ore[k][0]
		y = y + ore[k][1]
	#如果到头则回退一格换方向前进一格
	else:
	 	x = x - ore[k][0]
	 	y = y - ore[k][1]
		#换方向
	 	k = (k+1)%4
		x = x + ore[k][0]
		y = y + ore[k][1]
for id in range(i):
	print "\t".join(mylist[id])
