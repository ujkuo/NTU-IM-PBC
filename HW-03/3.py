nlstStr = input()
trlstStr = input()
threshold = []
slope = []

nlst = nlstStr.split(',')
for i in range(len(nlst)):
    nlst[i] = int(nlst[i])
n_period = nlst[0]
demand = nlst[1]

trlst = trlstStr.split(',')
for i in range(n_period): # 01234567
    threshold.append(int(trlst[i]))

for i in range(n_period, len(trlst)):
    slope.append(int(trlst[i]))

### below is the main algorithm ###

def count_threshold_cost(n, threshold, slope):
    temp = 0
    cost = 0
    t_count = []
    for i in range(n):
        cost += (threshold[i]-temp) * slope[i]
        t_count.append(cost)
        temp = threshold[i]

    return t_count

def count_x(n, demand, threshold, slope):
    temp = 0
    cost = 0
    for i in range(n):
        if demand > threshold[i]:
            cost += (threshold[i] - temp) * slope[i]
        else:
            cost += (demand - threshold[i-1]) * slope[i]
            break

    temp = threshold[i]
    return cost

tc = count_threshold_cost(n_period, threshold, slope)
dc = count_x(n_period, demand, threshold, slope)

min_value = 0
for i in range(n_period-1,0):
     if tc[i] < dc:
         min_value = tc[i]

print(min_value)


