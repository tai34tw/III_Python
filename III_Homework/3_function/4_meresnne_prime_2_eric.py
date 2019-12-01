'''
4.	函數的練習-mersenne_prime
寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
提示：若質數滿足2P-1=n (p為正整數)，則n為Mersenne Prime。
說明：當p=3時，23-1=7，故7為Mersenne Prime。

'''


def is_mersenne_prime():
    count = 0 #第幾個mersenne_prime
    n = 2
    list=[]
    while True:
        #print(count)
        if count < 5:
            Mersenne = pow(2, n) - 1
            #print(Mersenne)
            for i in range(2,Mersenne):
                if (Mersenne % i == 0):
                    break
            else:
                count+=1
                list.append(Mersenne)
        elif count == 5:
            return list
        n+=1
def main():
    list2 = is_mersenne_prime()
    print(list2)

if __name__ == '__main__':
    main()