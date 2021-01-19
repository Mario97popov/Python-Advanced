from collections import deque

Start_command = 'Start'
End_command = 'End'
Refill_command = 'refill'
total_amount = int(input())

peoples_queue = deque()

while True:
    command = input()
    if command == Start_command:
        break
    peoples_queue.append(command)

while True:
    command = input()
    if command == End_command:
        print(f'{total_amount} liters left')
        break
    if command.startswith(Refill_command):
        command_params = command.split(' ')
        refill_liters = int(command_params[1])
        total_amount += refill_liters
    else:
        person = peoples_queue.popleft()
        person_liters = int(command)
        if person_liters <= total_amount:
            print(f'{person} got water')
            total_amount -= person_liters
        else:
            print(f'{person} must wait')