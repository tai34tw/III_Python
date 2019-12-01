'''1.	一維串列的練習-max_min
事先將10個數字置於串列中，分別找出10個數字中最大的值和最小的值。
(勿使用現成的函數)
'''

def max(x):
    x.sort()
    max = x[9]
    return max
def min(x):
    x.sort()
    min = x[0]
    return min


def main():
    import random
    r_list = []
    for x in range(1, 10 + 1):
        r_list.append(random.randint(1, 20))
    print(r_list)
    print(max(r_list))
    print(min(r_list))
main()


