import math
a=0
b=0
c=0
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d=  math.sqrt(b**2-4*a*c)
root1 = ((-b + d)/2*a)
root2 = ((-b + d)/2*a)
print('근1:',f'{root1:.2f}')
print('근1:',f'{root2:.2f}')