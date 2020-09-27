input1 = input().split(",")
delivery = input().split(",")

stock = int(input1[0])
loading_time = int(input1[1])
week = 0
delivery = []
for i in range(7):
    delivery[i] = int(delivery[i])

while stock >= 0:
    for i in range(len(delivery)):
        stock -= delivery[i]
        if stock < 0:
            order_day = week * 7 + i + 1 - loading_time
            break
        week += 1

print(order_day)

