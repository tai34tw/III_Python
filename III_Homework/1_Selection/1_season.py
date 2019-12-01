'''1.	選擇性敘述的練習-season
輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
'''

month = eval(input('input month:'))
if month in range(1, 12):
    if month in (12, 1, 2):
        print('冬')
    elif month in (11, 10, 9):
        print('秋')
    elif month in (8, 7 ,6):
        print('夏')
    elif month in (5, 4 ,3):
        print('春')
else :
    print('輸入錯誤')

