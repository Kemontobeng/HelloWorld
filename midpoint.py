import math

#the standard formula for the midpoint formula is M[(x1 + x2)\2 ; (y1 + y2)\2]
#in other scenarios you may be given the midpoint coordinate and expected to calculate the x or y value of point 1 or point 2

#choice 1
def calcMidpoint (x1 , x2 , y1 , y2) : 
    midpointx = (x1 + x2)/2
    midpointy = (y1 + y2)/2

    midpoint = [midpointx , midpointy]
    return midpoint

#choice 2
def calcX1 (x2 , Mx):
    x1 = 2*(Mx) - x2
    return x1

#choice 3
def calcX2(x1 , Mx):
    x2 = 2*(Mx) - x1
    return x2

#choice 4
def calcY1(y2 , My):
    y1 = 2*(My) - y2
    return y1

#choice 5
def calcY2(y1 , My):
    y2 = 2*(My) - y1
    return y2

print('what do you want to calculate?')
print('1.calculate midpoint')
print('2.calculate x1')
print('3.calculate x2')
print('4.calculate y1')
print('5.calculate y2')

choice = input('Enter choice(1/2/3/4/5): ')


if choice =='1' :
    x1val = float(input('Enter x value of point 1 : '))
    y1val = float(input('Enter y value of point 1 : '))
    x2val = float(input('Enter x value of point 2 : '))
    y2val = float(input('Enter y value of point 2 : '))
    print('midpoint is ',calcMidpoint(x1val , x2val , y1val , y2val))

if choice == '2' : 
    x2val = float(input('Enter x value of point 2 : '))
    Mxval = float(input('Enter x value of midpoint : '))
    print ('x1 value is' ,calcX1(x2val , Mxval))

if choice == '3' : 
    x1val = float(input('Enter x value of point 1 : '))
    Mxval = float(input('Enter x value of midpoint : '))
    print ('x2 value is ',calcX2(x1val, Mxval))

if choice == '4' : 
    y2val = float(input('Enter y value of point 2 : '))
    Myval = float(input('Enter y value of midpoint : '))
    print ('x2 value is ',calcY1(y2val, Myval))

if choice == '5' : 
    y1val = float(input('Enter y value of point 1 : '))
    Myval = float(input('Enter y value of midpoint : '))
    print ('x2 value is ',calcY2(y1val, Myval))       


















  


