# Script to read stdin line by line, transform, and return it

i = 1
while True:
    try:
        user_input = input()
        print(i, user_input.upper())
        i += 1
    except EOFError:
        break
