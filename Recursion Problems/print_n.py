# def print_n(num):
#     if(num==1):
#         print(1)
#     else:
#         print_n(num-1)
#         print(num)


def print_n(num):
    if(num==1):
        print(num)
        return
    print(num)
    print_n(num-1)



print_n(7)