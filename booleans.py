import sys

python_is_glorious = True
failure_is_option = False
proper_greeting = False
greeting_string = "For the glory of Python!"

input_string = sys.argv[1]
if  (sys.argv[1] == greeting_string):
    proper_greeting = True
else :
    proper_greeting = False
    print("Incorrect Greeting!!!!")
