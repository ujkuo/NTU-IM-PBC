def divide(num):
    divided_num = []
    divided_num.append(int(num / 100))
    divided_num.append(int((num / 10) % 10))
    divided_num.append(int(num % 10))
    return divided_num

def eliminate(divided_num):
    divided_num.sort()
    ans = abs(100*divided_num[0]+10*divided_num[1]+divided_num[2] - (100*divided_num[2]+10*divided_num[1]+divided_num[0]))
    return ans

num = int(input())
ans = []
for i in range(3):
    temp = int(eliminate(divide(num)))
    ans.append(temp)
    # print(temp)
    num = temp
    
print(*ans, sep = ",")
