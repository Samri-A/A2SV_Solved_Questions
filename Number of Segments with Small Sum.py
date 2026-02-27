n , sum_ =map( int , input().split())
segment = list(map( int, input().split()))
left = 0
right = 0
segment_sum = 0
answer = 0
while right < n:
    segment_sum += segment[right]
    while segment_sum  > sum_:
        segment_sum -= segment[left]
        left+=1
    
    if segment_sum  <= sum_  : answer+= right - left + 1
    right+= 1

print(answer)
    



