nlstStr = input()
trlstStr = input()
threshold = [] # each turning point
slope = [] # price change

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

### Above is to get data        ###
### below is the main algorithm ###

def count_threshold_cost(n, threshold, slope): # calculate the count at turning points
    temp = 0
    cost = 0
    t_count = []
    for i in range(n):
        cost += (threshold[i]-temp) * slope[i]
        t_count.append(cost)
        temp = threshold[i]

    return t_count

def count_x(n, demand, threshold, slope): # calculate cost of demand(target)
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

tc = count_threshold_cost(n_period, threshold, slope) # just get the list from the function count threshold cost
dc = count_x(n_period, demand, threshold, slope) # just get the value from the function count x


### find the best pair of amount and value. Codes below are broken.


for i in range(n_period):
    print(i,tc[i],threshold[i])
min_value = 0
max_amount = 0
for i in range(n_period):
    min_value = tc[i]
    if tc[i] < dc and threshold[i] > demand and tc[i] < min_value:
       min_value = tc[i]
       max_amount = threshold[i]

print(max(max_amount,demand), min(min_value,dc), sep = ",")


