'''一元二次方程式ax**2+bx+c=0。輸入a, b, c三值，並計算方程式的根。
b**2-4ac > 0，有兩個不相等的實根。
b**2-4ac = 0，有兩個相等的實根。
b**2-4ac < 0，則印出”沒有實根”。
'''

a, b, c = eval(input('input a, b, c ='))
sqrt = (b ** 2 - 4 * a * c) **0.5
if   (b ** 2 - 4 * a * c) > 0:
        print ("根＝",sqrt,",有兩個不相等的實根。")
elif (b ** 2 - 4 * a * c) == 0:
        print("根＝",sqrt, ",有兩個相等的實根。")
elif (b ** 2 - 4 * a * c) < 0:
        print("根＝", sqrt, ",沒有實根。")
else:
    print("輸入錯誤")