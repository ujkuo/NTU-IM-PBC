age = int(input())
gender = int(input())
is_wearing = int(input())
is_visiting = int(input())
num_of_contacts = int(input())

if(num_of_contacts > 100):
    if is_visiting == 1:
        if is_wearing == 1:
            prob = 0.1
        else:
            prob = 0.95
    else:
        prob = 0.5
else:
    if age > 40:
        if gender == 1:
            prob = 0.6
        else:
            prob = 0.7
    else:
        prob = 0.2

print(prob)
