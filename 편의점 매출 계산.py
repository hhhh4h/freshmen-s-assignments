totalPrice = 0
buyCanCoffe = 0
buyTriangleKimbab = 0
buyBananaMilk = 0
buyLunch = 0
buyCola =  0
buySaewooggang = 0
soldCanCoffe = 0
soldTriangelKimbab = 0
soldBananaMilk = 0
soldLunch = 0
soldCola = 0
soldSaewooggang = 0
itemCost=0
soldCost = 0

print('밑의 항목에 구입한 물품의 갯수를 입력해주세요')
buyCanCoffe = int(input('캔커피:'))
buyTriangleKimbab = int(input('삼각김밥:'))
buyBananaMilk = int(input('바나나 우유:'))
buyLunch = int(input('도시락:'))
buyCola = int(input('콜라:'))
buySaewooggang = int(input('새우깡:'))

itemCost  = buyCanCoffe*500+buyTriangleKimbab*900+buyBananaMilk*800+buyLunch*3500+buyCola*700+buySaewooggang*1000
print('밑의 항목에 판매한 물품의 갯수를 입력해주세요')
soldCanCoffe = int(input('캔커피:'))
soldTriangleKimbab = int(input('삼각김밥:'))
soldBananaMilk = int(input('바나나 우유:'))
soldLunch = int(input('도시락:'))
soldCola = int(input('콜라:'))
soldSaewooggang = int(input('새우깡:'))
soldCost = soldCanCoffe*1800+soldTriangleKimbab*1400+soldBananaMilk*1800+soldLunch*4000+soldCola*1500+soldSaewooggang*2000
totalPrice = itemCost -soldCost
print('오늘의 수입:%d'%(totalPrice))