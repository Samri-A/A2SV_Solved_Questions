n = int(input())

for _ in range(n):
    n , k = map( int , input().split())
    s = input()
    not_B = 0
    left = 0
    right = 0
    minmum_recolor = n
    while right < n:
        if s[right] != 'B':
            not_B+=1
        
        while right - left + 1 > k:
            if s[left] != 'B':
                not_B-=1
            left+=1

        if right - left + 1 == k:
            minmum_recolor = min( not_B , minmum_recolor) 

        right+=1

    print(minmum_recolor)
