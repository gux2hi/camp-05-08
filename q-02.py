A = int(input())
B = list(map(int, input().split()))
C = list(map(int, input().split()))

T =""
for i in range(A):
    if B[i]==C[i]:
        T += str(i+1) + ""
if len(T)!=0:print(T)
else:print('0')