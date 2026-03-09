import heapq
m = int(input())

for _ in range(m):
    n , k = map(int , input().split())

    val_list =[]
    for i in range(n):
        casio = list(map(int , input().split()))
        val_list.append(casio)

    
    val_list.sort()

    casion_heap = []

    i = 0

    while True:

        while i < len(val_list) and  val_list[i][0] <= k :
            heapq.heappush(casion_heap ,( -val_list[i][2] , val_list[i][1]))
            i+=1

        
        while casion_heap and casion_heap[0][1] < k:
            heapq.heappop(casion_heap)
            
        if not casion_heap:
            break

        real, r = heapq.heappop(casion_heap)
        if -real > k : k = -real
        
   

    print(k)










