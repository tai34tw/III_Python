'''
2.	函數的練習-is_prime
寫一函數is_prime(n)用來判斷n是否為質數。
'''

def is_prime(n):
    total = 0
    for i in range(2, n+1):
        if n % i == 0:
            total += i
    if total == n:
        return True
    else:
        return False

def main():
    i = eval(input('input one number:'))
    i_is_prime = is_prime(i)
    if i_is_prime == 1:
        print(i, 'is prime')
    elif i_is_prime == 0:
        print(i, 'isn\'t prime')
main()
