import sys

count = 1
for arg in sys.argv[1:]:
    print(f"{count}. {arg}")
    count += 1