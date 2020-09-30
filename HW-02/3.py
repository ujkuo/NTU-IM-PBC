num = int(input())
weight = int(input())
cost = 0
lower_bound = 0
interval = []
price = []

for i in range(num):
    interval.append(int(input()))
    price.append(int(input()))

    if weight >= interval[i]:
        cost += (interval[i] - lower_bound) * price[i]
    else:
        if weight >= lower_bound:
            cost += (weight - lower_bound) * price[i]

    lower_bound = interval[i]

print(cost)


