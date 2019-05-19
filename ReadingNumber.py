#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input("x = "))
dictRead = {
	1: "một",
	2: "hai",
	3: "ba",
	4: "bốn",
	5: "năm",
	6: "sáu",
	7: "bảy",
	8: "tám",
	9: "chín"
}

if x in dictRead:
	print("{0} : {1}".format(x,dictRead[x]))
elif x == 10:
	print("10 : mười")
elif x == 15:
	print("15: mười lăm")
else:
	if x<20:
		print("{0} : mười {1}".format(x,dictRead[x%10]))  
	else:
		if x % 10 ==0:
			print("{0} : {1} mươi".format(x,dictRead[x//10]))
		elif x%5==0 and x%10!=0:
			print("{0} : {1} mươi lăm".format(x,dictRead[x//10]))
		else:
			print("{0} : {1} mươi {2}".format(x,dictRead[x//10],dictRead[x%10]))
