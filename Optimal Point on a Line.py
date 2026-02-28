n = int(input())
points = list(map(int, input().split()))

points.sort()

# we sorrt and find the midle point 

if n%2 == 0:
    print(points[(n//2 )-1])
else:
    print(points[n//2])
