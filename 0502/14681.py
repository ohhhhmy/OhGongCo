x = int(input())
y = int(input())

quadrant = 0

if x*y < 0:
    quadrant = 4 if x > 0 else 2
else:
    quadrant = 1 if x > 0 else 3
    
print(quadrant)