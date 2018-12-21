with open('day5inp.txt', 'r') as f:
    content = f.readline()


def calc(line):
    for i in range(0, len(line) - 1, 1):
        if not line[i] == line[i + 1]:
            if line[i].upper() == line[i + 1] or line[i] == line[i + 1].upper():
                line = line[:i] + line[i + 2:]
                return line
    return line


data = {}
origin = content
for i in range(97, 123, 1):
    if chr(i) in origin:
        content = origin
        content = content.replace(str(chr(i).upper()), '', 100000).replace(str(chr(i)), '', 100000)

        last = content
        content = calc(content)
        while not last == content:
            last = content
            content = calc(content)

        data[chr(i)] = len(content)

best = 1000000
for i in data:
    if data[i] < best:
        best = data[i]

print(best)
