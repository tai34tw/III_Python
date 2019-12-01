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

def product_total(sale):
    total = 0
    total_list =[]
    for i in range (1, len(sale[0])):
        for j in range (0, len(sale)):
            total += sale[j][i]
        total_list.append(total)
        total = 0
    return total_list


def super_product(sale):
    product_total1 = product_total(sale)
    product_index1 = product_total1.index(max(product_total(sale)))
    return product_index1

def main_c():
    sale = [['Jean', 33, 32, 56, 45, 33], ['Tom', 77, 33, 68, 45, 23], ['Tina', 43, 55, 43, 67, 65]]
    def greet (x, y):
        for i in x:
            for j in y:
                if x.index(i) == y.index(j):
                    print("{0}的銷售額為{1}".format(i, j))
    y = product_total(sale)
    x = ['產品A', '產品B', '產品C', '產品D','產品E']
    print('c.')
    greet(x, y)
main_c()


def main_d():
    sale = [['Jean', 33, 32, 56, 45, 33], ['Tom', 77, 33, 68, 45, 23], ['Tina', 43, 55, 43, 67, 65]]
    product_name = ['產品A', '產品B', '產品C', '產品D', '產品E']
    print('d', end = ". ")
    print(product_name[super_product(sale)])
main_d()








