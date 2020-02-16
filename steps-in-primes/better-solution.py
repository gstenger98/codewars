from math import sqrt

def step(g, m, n):
    primelist = []
    # print(n)
    upper_range = int(sqrt(n)) + 1
    # print(upper_range)
    for i in range(2,upper_range):
        isprime = True
        for _ in primelist:
            if i / _ == i // _:
                isprime = False
                break
        if isprime == True:
            primelist.append(i)
            # print(primelist)
    # print(primelist)
    new_primelist = []
    for a in range(m,n):
        isprime = True
        for b in primelist:
            if a / b == a // b:
                isprime = False
                break
        if isprime == True and a >= m and a <= n:
            # print('Current new_primelist: ' + str(new_primelist))
            # print('a: ' + str(a))
            for z in range(len(new_primelist)):
                # print('tempval: ' + str(new_primelist[(-1) * z]))
                if a - new_primelist[(-1) * z] == g:
                    # print('We\'ve got an answer!')
                    # print(str(new_primelist[(-1) * z]) + str(a))
                    return [new_primelist[(-1) * z], a]
            new_primelist.append(a)
    # print(new_primelist)
    return None
