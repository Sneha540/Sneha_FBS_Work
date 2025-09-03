n = 10  
num = 100

for i in range(n):
    line = []
    for j in range(10):
        line.append(num)
        num -= 1
    if i % 2 == 0:   
        line.reverse()
    for val in line: 
        print(val, end=" ")
    print()   
