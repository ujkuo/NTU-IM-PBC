if __name__ == "__main__":
nswer = []
for i in range(4):
        num.append(int(input()))
result = num[2] - num[1]
for i in range(2):
    delta = num[i*2+1] - num[i*2]
    answer.append(delta)
    result *= answer[i]
answer.append(result)

print(answer[0],answer[1],answer[2], sep = ',')


