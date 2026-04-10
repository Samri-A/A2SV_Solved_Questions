m = int(input())


def sort_(val , nums , swaps):
    swapped = True

    for j in range(0, len(nums)):
        for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                     nums[i-1] , nums[i] = nums[i] , nums[i-1]
                     swaps.append([val, i])

for _ in range(m):
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))


    swaps = []

    

    sort_(1 , a, swaps)
    sort_(2 , b, swaps)

    for i in range(len(a)):
        if a[i] > b[i]:
            swaps.append([3 , i+1])


    


    
                
    
    
    print(len(swaps))
    
    for swap in swaps:
        print(swap[0] , swap[1])
    # print(a , b)
