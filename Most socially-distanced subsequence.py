n = int(input())
for _ in range(n):
    n = input()
    p = input().split(' ')

    nums = []
    for i in p:
        nums.append(int(i))

    left = 0 
    right = 1

    answer = [str( nums[0])]

    for i in range(len(nums)):
        if i + 1 < len(nums) and i - 1 >= 0:
            if nums[i+1] < nums[i] > nums[i - 1] :
                answer.append(str(nums[i]))

    answer.append(str(nums[-1]) )

    print(len(answer))
    print(' '.join(answer))
    

    
    
