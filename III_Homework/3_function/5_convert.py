'''
5.	函數的練習-convert
輸入一整數，寫兩個函數分別為to_binary(n)和to_hexadecimal(n)用來將n轉換成二進制和十六進制的值。(勿使用任何現成的函數)
'''
#轉換2進位
def to_binary(n):
    return format(n,'b')

def main():
    n = eval(input("請輸入數字:"))
    print(n,'之二進位為',to_binary(n))
main()
#轉換16進位
def to_hexadecimal(n):
    return format(n, 'x')

def main():
    n = eval(input("請輸入數字:"))
    print(n,'之十六進位為',to_hexadecimal(n))
main()