values = input()
list_of_letters = list(values)

values_counts = {}

for value in list_of_letters:
    if value not in values_counts:
        values_counts[value] = 0
    values_counts[value] += 1

sorted_data = sorted(values_counts.items(), key=lambda x: x[0])

for (value, count) in sorted_data:
    print(f'{value}: {count} time/s')


