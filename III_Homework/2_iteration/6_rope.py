'''6.	迴圏的練習-rope
若有一條繩子長3000公尺，每天剪去一半的長度，需多少天繩子的長度會短於5公尺。'''
n = 0
length = 3000
while length > 5:
    length *= 0.5
    n += 1
print(n)


