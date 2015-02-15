#!/usr/bin/python
import math
import sys

#func : amount of water /V=sqrt(2) / 12 * a^3/
def fill_tetrahedron(num):
	
 return ((math.sqrt(2)* num**3)/12) * 10**-3 ;

# Function definition is here  
def tetrahedron_filled(listCm,num):
	
	amount=0;
	total=0
	listCm.sort();
	for x in listCm :
		current=fill_tetrahedron(x);
		if total+current<num:
			amount+=1;
			total+=current;

	return amount
 

# main

lengthsList=[]

while len(lengthsList)<3:
	cm=int(input("Enter cm : "))
	lengthsList.append(cm)

water=int(input("Amount of water : "))
ans=int(tetrahedron_filled(lengthsList,water));
print  (ans );