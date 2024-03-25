l, c = list(map(int, input().split()))
a, b = list(map(int, input().split()))
a-=1
b-=1

matrix = []
for i in range(l):
    line = input().split()
    matrix.append(line)

while True:
    
    matrix[a][b] = 'X'
    if a-1 >= 0:        
        if matrix[a-1][b] == '1':
            a = a-1
            continue
    if a+1 < l:
        if matrix[a+1][b] == '1':        
            a = a + 1
            continue
    if b-1 >= 0:        
        if matrix[a][b-1] == '1':
            b = b-1
            continue
    if b+1 < c:        
        if matrix[a][b+1] == '1':
            b = b+1
            continue
    break        

print(f'{a+1} {b+1}')
