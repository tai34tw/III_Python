'''
3.	二維串列的練習-sales
某一公司有五種產品A、B、C、D與E，其單價分別為12、16、10、14與15元；而該公司共有三位銷售員，他們在某月份的銷售數量如下所示

銷售員   產品A	產品B	產品C	產品D	產品E
Jean	33	    32	    56	    45	    33
Tom	    77	    33	    68	    45	    23
Tina	43	    55	    43	    67	    65

試計算：
a.	每一個銷售員的銷售總金額
b.	有最好業績（銷售總金額最多者）的銷售員
c.	每一項產品的銷售總金額
d.	銷售總金額最多的產品

'''

def name_list(sale):
    name_list1 = []
    for i in range (len(sale)):
        name_list1.append(sale[i][0])
    return name_list1

def sum_list(sale):
    sum_list = []
    for i in range (len(sale)):
        sum_sale = sum((sale[i][1:]))
        sum_list.append(sum_sale)
    return sum_list

def sum_list_max(sumlist):
    sum_list_max = max(sum_list(sumlist))
    return sum_list_max

def super_sales(sale):
    sum_list_max1 = sum_list_max(sale)
    sum_list1 = sum_list(sale)
    sum_list1.index(sum_list_max(sale))
    sale_index = sum_list1.index(sum_list_max1)
    return sale[sale_index][0]




def main():
    sale = [['Jean', 33, 32, 56, 45, 33], ['Tom', 77, 33, 68, 45, 23], ['Tina', 43, 55, 43, 67, 65]]
    #a
    name_list1 = name_list(sale)
    sum_list1 = sum_list(sale)
    print('a')
    for i in name_list1:
        for j in sum_list1:
            if name_list1.index(i) == sum_list1.index(j):
                print  ("{0}的銷售額為{1}".format(i, j))
    #b
    print('b.',super_sales(sale))

main()







