'''3.	選擇性敘述的練習-electricity
輸入何種用電和度數，計算出需繳之電費。
電力公司使用累計方式來計算電費，分工業用電及家庭用電。
'''

type   = eval(input('請輸入數字:1:工業用電 or 2:家庭用電:'))
degree = eval(input('input: electrical degree:'))
if  type == 2:
    if   degree >= 540:
            d1 = 240; d2 = (540 - d1); d3 = (degree-(d1+d2))
    elif 240 < degree <= 540:
            d1 = 240; d2 = (degree - d1); d3 = 0
    else:
            d1 = degree; d2, d3 = 0, 0
    print(d1 * 0.15 + d2 * 0.25 + d3 * 0.45)
elif type == 1:
    print(degree * 0.45)
else:
    print('輸入錯誤;請輸入數字:1:工業用電 or 2:家庭用電:')

