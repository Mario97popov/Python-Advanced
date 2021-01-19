text = input()
splited = text.split(" ")

s = []

for ch in splited:
    if len(ch) > 0 and ((ch.isnumeric()) or
                        ch.startswith("-") and ch[1:].isnumeric()):
        s.append(int(ch))

result = []

while s:
    result.append(s.pop())

print(*result, sep=" ")
