'''
2.	函數與串列的練習-pass_list
a~d各小題皆以一函數來處理：為練習串列的參數傳遞，陣列需定義為main()的區域變數，
事先將12個數字置於一3 x 4的二維串列中，列印各函數的結果。
a.	計算所有數字的平均值
b.	找出12個數字中最大的值
c.	找出12個數字中最小的值
d.	計算每組內4個數字的平均值

'''
def avg＿matrix(n):
    import statistics
    list_avg = []
    for i in range (0, len(n)):
        for j in range (0, len(n[0])):
            list_avg.append(n[i][j])
    return statistics.mean(list_avg)


def max_matrix(n):
    list_max= []
    for i in range(0, len(n)):
        for j in range(0, len(n[0])):
            list_max.append(n[i][j])
    return max(list_max)

def min_matrix(n):
    list_min= []
    for i in range(0, len(n)):
        for j in range(0, len(n[0])):
            list_min.append(n[i][j])
    return min(list_min)

def avg_sep(n):
    import statistics
    avg_list = []
    for i in range(0, len(n)):
        avg =  statistics.mean(n[i])
        avg_list.append(avg)
    return avg_list



def main():
    matrix34 = [1, 2, 3, 4], [ 5, 6, 7, 8], [9, 10 ,11 ,12]
    print(avg_matrix(matrix34))
    print(max_matrix(matrix34))
    print(min_matrix(matrix34))
    print(avg_sep(matrix34))
main()