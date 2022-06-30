import sys

integer_list = []

def read_int_args(args):
    for arg in args:
        integer_list.append(int(arg))

read_int_args(sys.argv[1:])

def fizzbuzzer(integer_list):
    for integer in integer_list:
        message = ''
        if integer % 3 == 0:
            message += 'fizz'
        if integer % 5 == 0:
            message += 'buzz'
        if len(message) < 1:
            message = integer
        print(message)
        
fizzbuzzer(integer_list)