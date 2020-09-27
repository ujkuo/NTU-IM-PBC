h = int(input())
k = int(input())
threshold = int(input())
disappointment = int(input())
n = int(input())
day = []
accummodation = 0
total_time = 0
times = 0

for i in range(n):
    day.append(int(input()))

for i in range(n):

    if accummodation >= disappointment:
        times += 1
        disappointment *= (times + 1)
        if times == threshold:
           # print(times)
            print("哆拉A夢要回到未來了！")
            break
        else:
            print("哆拉A夢生氣了！")
    if day[i] <= h:
        if accummodation <= 0:
            accummodation += 0
        else:
            accummodation += day[i] - h
        total_time += day[i]
    else:
        accummodation += k * day[i]
        total_time += day[i]
            

print(total_time)
