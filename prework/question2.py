
def odd_number():
    num = list(range(0,101))
    for no in num:
        if no % 2 != 0:
            print(no)

def odd_number1():
    for i in range(0,101,2):
        print(i)

odd_number1()