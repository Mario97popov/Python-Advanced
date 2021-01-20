def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(numbers):
    for num in numbers:
        print(num)


a, b = map(int, input().split())

n2 = input_to_list(a)

m2 = input_to_list(b)
# n2 = [
#     '1',
#     '3',
#     '5',
#     '7',
# ]
# n3 = [
#     '3',
#     '4',
#     '5',
# ]
set_with_n = set()
set_with_m = set()
set_with_all_el = set()

for number in n2:
    set_with_n.add(number)
for number in m2:
    set_with_m.add(number)
for el in set_with_m:
    for _ in set_with_n:
        if el == _:
            set_with_all_el.add(el)

print_result(set_with_all_el)
