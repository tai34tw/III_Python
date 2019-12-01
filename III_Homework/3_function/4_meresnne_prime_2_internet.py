'''4.	函數的練習-mersenne_prime
寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
提示：若質數滿足2P-1=n (p為正整數)，則n為Mersenne Prime。
說明：當p=3時，2**3-1=7，故7為Mersenne Prime。
'''
def lucas_lehmer(p):
    s = 4
    m = 2 ** p - 1
    for _ in range(p - 2):
        s = ((s * s) - 2) % m
    return s == 0

def is_prime(number):
    """
    the efficiency of this doesn't matter much as we're
    only using it to test the primeness of the exponents
    not the mersenne primes themselves
    """

    if number % 2 == 0:
        return number == 2

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True

print(3)  # to simplify code, treat first mersenne prime as a special case

for i in range(3, 5000, 2):  # generate up to M20, found in 1961
    if is_prime(i) and lucas_lehmer(i):
        print(2 ** i - 1)