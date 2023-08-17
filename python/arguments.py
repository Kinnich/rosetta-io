import sys

if len(sys.argv) != 2:
    print("Make sure you're inputting an arg in the dockefile")
    sys.exit(1)

print(sys.argv[1].lower())
