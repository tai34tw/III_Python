'''1.	函數的練習-sigma
寫一函數my_fun (x, n)如下：
'''

def myfun(x, n):
    fac = 1
    result = 0
    for n in range(1, (n+1)):
        fac *= n
        result += ((x ** n) / fac)
    return result

def main():
    (x, n) = eval(input('Type 2 numbers:'))
    print(myfun(x, n))
main()






