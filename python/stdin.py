# Test script to get input, transform, and return it
# Testing that it reads line by line
# and that it does the transformation (to make sure that we're
# getting the stdin throught python)
i = 1
while True:
    try:
        user_input = input()
        print(i, user_input.upper())
        i += 1
    except EOFError:
        break
