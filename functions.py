
from wsgiref.simple_server import WSGIRequestHandler

def hail_friend(friend_name="friend"):
    print(f"Hail, {friend_name}!")

hail_friend('Jonathan Joestar')

def add_numbers(first_number, second_number):
    return first_number + second_number

print(f'1 plus 1 is {add_numbers(1,1)}')