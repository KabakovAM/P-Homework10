def init(num_1, num_2, op, typ):
    if op == 3:
        return num_1*num_2
    if op == 5 and typ == 1:
        return num_1**num_2
    res = num_1**num_2
    return round(res.real, 2)+round(res.imag, 2)*1j
