n = int(input())
contest = list(map(int , input().split()))

contest.sort()

pointer =  0
k = 1
days = 0

while pointer < len(contest):
    if contest[pointer] >= k:
            days+=1
            k+=1

    pointer+=1
    

print(days)
