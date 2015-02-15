#!/usr/bin/python
import math
import sys

# Function definition is here  /V=sqrt(2) / 12 * a^3/
def fill_tetrahedron(num):
	
 return ((math.sqrt(2)* num**3)/12) * 10**-3 ;

# main
num=int(input("Enter length in cm  : "));
ans=float(fill_tetrahedron(num));
print  ('%10.2f'%ans ,"liters");