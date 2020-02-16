def step(g, m, n):
    # print(g)
    # print(m)
    # print(n)
    primeset = set()
    for i in range(2,n):
        isprime = True
        for _ in primeset:
            if i / _ == i // _:
                isprime = False
                break
        if isprime == True:
            primeset.add(i)
            # print(primeset)
    mn_primelist = sorted([p for p in primeset if p >= m])
    # print(mn_primelist)
    for j in mn_primelist:
        # print('j = ' + str(j))
        for k in mn_primelist:
            # print('k = ' + str(k))
            if k - j == g:
                # print(j)
                # print(k)
                return [j,k]
            if k - j > g:
                break
    return None
