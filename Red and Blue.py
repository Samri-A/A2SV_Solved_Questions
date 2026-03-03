n = int(input())

for _ in range(n):
    n_r = int(input())
    r = list(map(int, input().split()))
    n_b = int(input())
    b = list(map(int, input().split()))

    
    maximum_sum_b = 0
    b_sum = 0
    for i in b:
        b_sum += i
        maximum_sum_b = max(b_sum , maximum_sum_b)

    maximum_sum_r = 0
    r_sum = 0
    for i in r:
        r_sum += i
        maximum_sum_r = max(r_sum , maximum_sum_r)

    maximum_sum = maximum_sum_r + maximum_sum_b
    print(maximum_sum)

        
