N = int(input())
a = [int(input()) for _ in range(N)]


now_direction = 0  
x = 0 
y = 0 

for i in range(N):
    match now_direction:
        case 0:
            y += a[i]
        case 1:
            x += a[i]
        case 2:
            y -= a[i]
        case 3:
            x -= a[i]
    now_direction = (now_direction + 1) % 4

print(f'{x} {y}')
