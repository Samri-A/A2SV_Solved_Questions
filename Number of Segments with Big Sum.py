n , sum_ =map( int , input().split())
segment = list(map( int, input().split()))
left = 0
right = 0
segment_sum = 0
answer = 0
while right < n:
    segment_sum += segment[right]
    temp = segment_sum
    while segment_sum >= sum_:
        segment_sum -= segment[left]
        left+=1
        answer+= n - right
    
    
    right+= 1



print(answer)
    



