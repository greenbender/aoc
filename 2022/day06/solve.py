import sys


data = sys.stdin.read().strip()


# part 1
for i in range(3, len(data)):
    s = set(data[i - 3 : i + 1])
    if len(s) == 4:
        print(i + 1)
        break


# part 2
for i in range(13, len(data)):
    s = set(data[i - 13 : i + 1])
    if len(s) == 14:
        print(i + 1)
        break
