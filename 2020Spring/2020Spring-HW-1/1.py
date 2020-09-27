num = []
answer = []
day = 0
for i in range(4):
    num.append(int(input()))

result = num[2] - num[1]
for i in range(2):
    delta = num[i*2+1] - num[i*2]
    answer.append(delta)
    result *= answer[i];
answer.append(result)

for i in range(3):
    delta = num[i+1] - num[i]
    if delta <= 14:
        day += 1
answer.append(day)

print(str(answer[0]) + "," + str(answer[1]) + "," + str(answer[2]) + ";" + str(answer[3]))
