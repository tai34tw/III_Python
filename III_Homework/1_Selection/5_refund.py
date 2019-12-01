'''5.	選擇性敘述的練習-refund
輸入在某商店購物應付金額與實付金額。
實付金額小於應付金額，則印出”金額不足”。
實付金額等於應付金額，則印出”不必找錢”。
實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。
'''

payment = eval(input('應付金額:')); money = eval(input('實付金額:'))
if payment == money: print('不必找錢')
elif money < payment: print('金額不足')
elif money > payment:
    diff         = money - payment
    thousand     = diff//1000
    five_hundred = diff % 1000 // 500
    one_hundred  = diff % 1000 % 500 // 100
    fifty        = diff % 1000 % 500 % 100 // 50
    ten          = diff % 1000 % 500 % 100 % 50 // 10
    five         = diff % 1000 % 500 % 100 % 50 % 10 // 5
    one          = diff % 1000 % 500 % 100 % 50 % 10 % 5
print("應找回",thousand,"張1,000元",five_hundred,"張500元",
              one_hundred,"張100元",fifty,"個50元硬幣",
              ten,"個10元硬幣", five,"個5元硬幣", one,"個10元硬幣")