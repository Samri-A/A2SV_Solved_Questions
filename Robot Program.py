n = int(input())


for _ in range(n):
    length , x , k = map( int ,input().split(' '))
    command = input()
    pzeros = 0
    s = 0
    time = 0
    p1 = 0

    for i in range(length):
        if command[i] == 'R': s +=1
        else: s-=1

        if s == -x and pzeros == 0:
            pzeros = i + 1

        if not p1 and not s:
            p1 = i + 1

    if pzeros == 0:
        print(0)
    elif p1 != 0: print( 1 + (k - pzeros ) // p1)
    else : print(1)
