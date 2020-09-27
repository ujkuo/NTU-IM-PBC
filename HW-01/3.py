x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())
limit = int(input())
answer = ""

remain_t = limit - x1 - x2
remain_m = t - x1*p1 - x2*p2

if remain_t >= 0:
    answer = str(remain_t) + ","

if remain_m >= 0:
    answer += "$" +str(remain_m)
    
print(answer)
