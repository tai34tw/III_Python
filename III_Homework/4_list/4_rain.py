'''
4.	三維串列的練習-rain
輸入一字串，字串為”all” 表示計算60個月的總平均降雨量，”year”、”season”和”month”分別表示計算某年、某季或某月的平均降雨量。若為後三者，再輸入一個正整數表示那一年、那一季或那一月。
說明：5年12個月的降雨量以三維陣列形式事先給好60個浮點數
需做誤錯處理：
a.	輸入除了”all”、”year”、”season”和”month”以外的字串
b.	若輸入”year”，而正整數輸入1至5以外的數字
c.	若輸入”season”，而正整數輸入1至4以外的數字
d.	若輸入”month”，而正整數輸入1至12以外的數字
'''

rain = [['year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
