weight = int(input())
interval = []
price = []
cost = 0
lower_bound = 0

for i in range(3):
    interval.append(int(input()))
    price.append(int(input()))

    if weight >= interval[i]:
        cost += (interval[i] - lower_bound) * price[i]
    else:
        if weight >= lower_bound:
            cost += (weight - lower_bound) * price[i]

    lower_bound = interval[i]

print(cost)


