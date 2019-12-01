'''
3.	函數的練習-prime
寫一函數get_prime (n)用來找出第n個質數。
'''


def is_prime(n):
    total = 0
    for i in range(2, n + 1):
        if n % i == 0:
            total += i
    if total == n:
        return True
    else:
        return False

def get_prime(prime_num):
    n = 1
    count = 0
    while True:
        n += 1
        if is_prime(n):
            count += 1
        if count == prime_num:
            break
    return n

def main():
    prime_num = eval(input('輸入第幾個質數：'))
    print(get_prime(prime_num))
main()
