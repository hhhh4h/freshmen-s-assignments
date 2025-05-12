t = int(input('주차한 분 수를 입력하세요:'))
a = (input('저공해/경차 등 할인 차량인가요?'))
if(t<=30):

    if a=='yes' :
        print('주차요금:1000원')
    elif a== 'no' :
        print('주차요금:2000원')
else:

    if a=='yes':
        t=t-30
        c= (t//10)
        if (t%10)==0:
            p = ((c*1000)+2000)/2
            print(f'주차요금:{p}')
    elif a=='no':
        t=t-30
        c = (t // 10)
        p = (((c * 1000) + 2000)+1000)
        print(f'주차요금:{p}')
