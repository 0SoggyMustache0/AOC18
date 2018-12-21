with open('day5inp.txt', 'r') as f:
    content = f.readline()


def calc(line):
    for i in range(0, len(line) - 1, 1):
        if not line[i] == line[i + 1]:
            if line[i].upper() == line[i + 1] or line[i] == line[i + 1].upper():
                line = line[:i] + line[i + 2:]
                return line
    return line


last = content
content = calc(content)
while not last == content:
    last = content
    content = calc(content)
#   print(content)

print(content)
print(len(content))
