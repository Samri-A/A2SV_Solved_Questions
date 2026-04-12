class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = deque()

        for i in range(1,n+1):
            friends.append(i)
        
        print(friends)

        tracker = 0
        while len(friends) > 1:
            tracker+=1

            if tracker == k:
                friends.popleft()
                tracker = 0
            else:
                val =  friends.popleft()
                friends.append(val)


        return friends.pop()
