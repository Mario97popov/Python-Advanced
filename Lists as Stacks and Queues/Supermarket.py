from collections import deque

End_command = "End"
Paid_command = "Paid"

names_queue = deque()

while True:
    command = input()
    if command == End_command:
        print(f'{len(names_queue)} people remaining.')
        break
    elif command == Paid_command:
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)
