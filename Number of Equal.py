n1 , n2 = map(int ,  input().split())
nums1 = list(map(int ,  input().split()))
nums2 = list(map(int ,  input().split()))

pointer1 = 0
pointer2 = 0
count_pair = 0
while pointer1 < n1 and pointer2 < n2:
    if nums1[pointer1] == nums2[pointer2]:
        
        count_1 = 1
        while pointer1 + 1 < n1 and nums1[pointer1+1] == nums2[pointer2]:
            count_1+=1
            pointer1+=1

        count_2 = 1
        while pointer2 + 1 < n2 and nums1[pointer1] == nums2[pointer2 + 1]:
            count_2+=1
            pointer2+=1
            
        # print(nums1[pointer1] , count_1)
        # print(nums2[pointer2] , count_2)

        count_pair += count_1 * count_2
        pointer2 +=1
        pointer1 +=1

        
    elif nums1[pointer1] > nums2[pointer2]:
        pointer2+=1
    else:
        pointer1+=1

print(count_pair)

