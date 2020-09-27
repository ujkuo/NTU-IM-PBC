c = int(input())
t = int(input()) #tempeature
d = int(input()) #d-temp
v = float(input())
w_0 = float(0.5)

h = int(100 - 5*(t-d))
if c <= 35:
    w_a = float(w_0 + (100-c)*0.005)
else:
    w_a = float(w_0 + (45-c)* 0.02)


if h > 30:
    w_h = float(w_0*(90-h)/45)
else:
    w_h = float(w_0*(110-h)/60)

if w_a > 1:
    w_a = 1
elif w_a < 0:
    w_a = 0

if w_h > 1:
    w_h = 1
elif w_h < 0:
    w_h = 0

w = float(min(w_a,w_h))
if w < v:
    print('{:.2f}'.format(w) + '\n' + "I wouldn't go out with you.")
else:
    print('{:.2f}'.format(w) + '\n' + "Let's go together.")
    
