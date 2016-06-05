# _*_ coding: utf-8 _*_
import re
mydict = {"+":4,"-":4,"*":5,"/":5,"(":7,")":7}
caldict = {"+":2,"-":2,"*":2,"/":2,"(":2,")":2}
#计算
def fcal(mystr):
	if mystr[-1]=="+":
		return str(float(mystr[1])+float(mystr[0]))
	if mystr[-1]=="-":
	 	return str(float(mystr[1])-float(mystr[0]))
	if mystr[-1]=="*":
		return str(float(mystr[1])*float(mystr[0]))
	if mystr[-1]=="/":
		return str(float(mystr[1])/float(mystr[0]))
'''
#从控制台读取运算式
def readFormula():
	formula = raw_input("input your formulate\n")
	return list(formula)
'''

#从控制台读取运算式
def readFormula():
	mylist = []
	end = []
	formula = raw_input("input your formulate\n")
	begin = list(formula)
	for id1 in begin:
		if re.match(r'[\d,.]',id1):
			mylist.append(id1)
		else:
			if mylist:
				end.append(''.join(mylist))
				mylist = []
			end.append(id1)
	if mylist:
		end.append(''.join(mylist))
	return end


#生成逆波兰表达式
def createRPN(mylist):
	flag = 0
	stack = []
	output = []
	for id1 in mylist:
		if re.match(r'\d+',id1):
			output.append(id1)
		if re.match(r'[+,\-,*,/,(,)]{1}',id1):
			if not stack or mydict[stack[-1]] < mydict[id1]:
				if id1 == ")":
					while stack[-1] != "(":
						output.append(stack.pop())
					stack.pop()
				else:
					stack.append(id1)
			else:
				while stack and mydict[stack[-1]]>=mydict[id1] and stack[-1] != "(":
						output.append(stack.pop())
				stack.append(id1)
	while stack:
		if stack[-1] not in ["(",")"]:
			output.append(stack.pop())
		else:
			stack.pop()
	return output

#根据逆波兰表达式计算值	
def calFormula(rpnlist):
	stack = []
	callist = []
	for id1 in rpnlist:
		if re.match(r'\d+',id1):
			stack.append(id1)
		else:
		 	for id2 in range(caldict[id1]):
				callist.append(stack.pop())
			callist.append(id1)
			stack.append(fcal(callist))
			callist = []
	if len(stack) == 1:
		return stack[-1]

if __name__ == '__main__':
	while True:
		print calFormula(createRPN(readFormula()))
#	print readFormula()
