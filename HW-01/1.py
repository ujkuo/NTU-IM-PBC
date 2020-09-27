x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())

remain = t - x1*p1 - x2*p2
if remain >= 0:
    print("$" + str(remain))
else:
    print(-1)

