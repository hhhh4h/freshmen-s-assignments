#두변 길이 합이 나머지 보다 길어야함 1 1 2 ,3 3 3
#3 + 2
#a= input('enter:')
#print(a)
a = input('enter:')
b = input('enter:')
c = input('enter:')
if  (a<b+c) and (b<a+c) and (c<a+b) :
    print('가능')
else:
    print('불가능')