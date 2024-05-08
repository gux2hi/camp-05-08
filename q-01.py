A = int(input())

x, y = 0, 0
direction = 0
steps = 0

for i in range(A):
    step = steps[i]
    if direction == 0:
        y += step
    elif direction == 1:
        x -= step
    elif direction == 2:
        y -= step
    elif direction == 3:
        x += step
print(x,y)