def init(num_1, num_2, op, typ):
    if op == 4 and typ == 1:
        return round(num_1/num_2, 2)
    if op == 6:
        return round((num_1**0.5), 2)
    res = num_1/num_2
    return round(res.real, 2)+round(res.imag, 2)*1j
