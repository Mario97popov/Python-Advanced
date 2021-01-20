def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def Convert(string):
    li = list(string.split(" "))
    li.pop(0)
    return li


def print_result(elements):
    for el in elements:
        print(el)


n = int(input())
elements = input_to_list(n)
# elements = [
#     'Ce O',
#     'Mo O Ce',
#     'Ee',
#     'Mo',
# ]

unique_elements = set()
lol = ''
for el in elements:
    lol += ' '
    lol += ''.join(el.split(','))
for _ in Convert(lol):
    if _ in unique_elements:
        pass
    else:
        unique_elements.add(_)

print_result(unique_elements)
