#!/usr/bin/python
import math
import sys

# Function to change
def caesar_encrypt(let,n):
	x=0;
	newStr="";
	while x < len(let) :
		add=ord(let[x])+n;
		newStr+=chr(add);
		x+=1;

	return newStr; 

#main
let=str(input("Letters  : "));
num=int(input("enter num : "));
ans=str(caesar_encrypt(let,num));
print  (ans);