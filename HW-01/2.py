x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())
limit = int(input())

remain_t = limit - x1 - x2
remain_m = t - x1*p1 - x2*p2

if remain_t >= 0:
    if remain_m >= 0:
        print(str(remain_t) + ",$" + str(remain_m))
    else:
        print(str(remain_t) + "," + str(-2))
else:
    if remain_m >= 0:
        print(str(-1) + ",$" + str(remain_m))
    else:
        print(str(-1) + "," + str(-2))





