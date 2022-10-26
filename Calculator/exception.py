
def type_op(num, n):
    if num.isdigit() and -1 < int(num) < n+1:
        return int(num)
    return False


def number(num):
    if num.lstrip('-').replace('.','',1).isdigit():
        if '.' in num:
            return float(num)
        return int(num)
    return False