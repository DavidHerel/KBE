def cube_root(x):
    #lower bound, upper bound, optimum
    lb = 1
    ub = 1
    opt = 1
    while True:
        if (pow(ub, 3) > x):
            lb = ub // 2
            opt = (lb + ub) // 2
            while True:
                if (lb > ub):
                    opt += 1
                    return opt
                elif (x < pow(opt, 3) and ub > opt):
                    ub = opt
                elif (x > pow(opt, 3) and lb < opt):
                    lb = opt
                else:
                    return opt
                opt = (lb + ub) // 2
        ub = ub * 2

def attack(n, data):
    N = 1
    M = 0
    for i in n:
        N = N * i
    index = 0
    for i in n:
        n_i = N//i
        u_i = pow(n_i, -1, i)
        M += data[index]*u_i*n_i
        index += 1
    return cube_root(M % N)