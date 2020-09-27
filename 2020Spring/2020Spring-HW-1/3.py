age = int(input())
gender = int(input())
is_wearing_mask = int(input())
is_visiting = int(input())
num_of_contacts = int(input())

prob = 0.5

if(age > 50):
    prob += 0.1
else:
    prob -= 0.1

if(gender == 1):
    prob *= 1.1
else:
    prob *= 0.9

if(is_wearing_mask == 1):
    prob *= 0.75
else:
    prob *= 1.25

if(is_visiting == 1):
    prob += 0.18
else:
    prob -= 0.18

if(num_of_contacts > 100):
    prob += (num_of_contacts // 15) / 100
else:
    prob -= ((100 - num_of_contacts) // 15) /100

if prob > 1:
    prob = 1
elif prob < 0:
    prob = 0;

print("%.2f" % prob)


