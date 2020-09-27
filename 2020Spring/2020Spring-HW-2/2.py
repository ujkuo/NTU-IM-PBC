num = []
answer = []
delta = []
add = []
day = 0
count = 0
for i in range(4):
    num.append(int(input()))

threshold = int(input())

for i in range(3):
    difference = num[i+1] - num[i]
    delta.append(int(difference))
    #print(delta[i])
    if(delta[i] < threshold):
        count += 1
        #print(count)
        adding = num[i+1] + threshold
        add.append(adding)
        #print(add[i])

print(min(count*threshold, add[-1]-num[0]))
