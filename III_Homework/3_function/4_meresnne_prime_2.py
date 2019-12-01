'''4.	函數的練習-mersenne_prime
寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
提示：若質數滿足2P-1=n (p為正整數)，則n為Mersenne Prime。
說明：當p=3時，2**3-1=7，故7為Mersenne Prime。
'''

# 驗證是否為Mersenne質數之數字
def is_mersenne_prime(n):
    def is_prime(n):
        total = 0
        for i in range(2, n + 1):
            if n % i == 0:
                total += i
        if total == n:
            return True
        else:
            return False

    if is_prime(n)%2:
        for p in range (1, n):
            if (2**p)-1 == n:
                return n
        else:
            return False
    else:
        return False

def main():
    n = 1
    count = 0
    while True:
        n += 1
        if is_mersenne_prime(n):
            count += 1
            print(is_mersenne_prime(n))
        if count == 10:
            break
main()


