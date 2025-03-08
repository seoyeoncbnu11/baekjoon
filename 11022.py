T = int(input())
for i in range(T):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)

    print('Case #{0}: {1} + {2} = {3}'.format(i+1, a, b, a+b))