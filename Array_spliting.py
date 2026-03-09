n , k =map(int , input().split())

nums = list(map(int , input().split()))
min_cost = max(nums) - min(nums)
difference = []

for i in range(1, n):
    difference.append(nums[i-1] - nums[i])

difference.sort()
k-=1

j = 0
while k > 0:
    min_cost += difference[j]
    k-=1
    j+=1
print(min_cost)



