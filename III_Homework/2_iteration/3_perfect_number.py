'''3.	迴圏的練習-perfect_number
一個數字若等於其所有因數的總和，則此數為perfect number。
找出100以內所有的完美數。
說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。
'''

for j in range(2,101):
    total = 0
    for i in range(1,j):
        if j % i == 0:
            total +=i
    if total == j:
        print(total, end = ", ")
print()

#下為網路解答
L = []
for i in range(1, 1001):
    k = 0
    for j in range(1, i):
        if (i % j == 0):
            k += j
    if i == k:
        L.append(i)
print(L)