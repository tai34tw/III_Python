'''4.	選擇性敘述的練習-leapYear
輸入一西元年，如2015。判斷此年份是否為閏年。
提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。
'''

ly = '閏年'; nly = '非閏年'
yr = eval(input('請輸入西元年份:'))
if yr%4000 == 0:
    print(nly)
elif yr%400 == 0 and yr%4000 != 0:
    print(ly)
elif yr%100 == 0 and yr%400 != 0:
    print(nly)
elif yr % 4 == 0 and yr % 100 != 0:
    print(ly)
else:
    print(nly)
