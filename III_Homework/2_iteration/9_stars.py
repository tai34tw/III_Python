'''9.	迴圈敘述的練習-stars
   畫出下列三種排列的星星圖形。
 (1)	*         (2)   * * * * *    (3)  	*
        * *              * * * *           *  *
        * * *              * * *          *  *  *
        * * * *              * *         *  *  *  *
        * * * * *              *        *  *  *  *  *

'''

#1
for n in range (1, 6):
    print('* ' * n)
print()

#2
for n in range (5, 0, -1):
    print('{0:>10s}'.format('* ' * n))
print()

#3
for n in range (1, 6):
    print('{0:^10s}'.format('* ' * n))
print()