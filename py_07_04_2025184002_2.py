a= input('enter:')
o1,op,o2 = a.split()
o1 = int(o1)
o2 = int(o2)

if (op == '+'):

    b=o1 + o2
    print(f'{b:.3f}')

elif (op == '-'):
    b = o1 - o2
    print(f'{b:.3f}')

elif (op == '/'):
    b = o1/o2
    print(f'{b:.3f}')
elif (op == '*'):
    b = o1*o2
    print(f'{b:.3f}')