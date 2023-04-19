def calculate_floor(a):
    b=0
    for i in range(4):
        if a[i]=='D':
            b-=1
        if a[i]=='U':
            b+=1
    print(b)
a=str(input())
calculate_floor(a)