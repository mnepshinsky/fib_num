def fib_num(index):
    if (index == 0):
        return 0
    elif (index == 1):
        return 1
    else: 
        return fib_num(index-1) + fib_num(index-2)


print(fib_num(15))