katz_deli = []

def line(queue):
    if len(queue) == 0:
        print('The line is currently empty.')

    else:
        announcement = 'The line is currently:'
        for i in range(len(queue)):
            place = i + 1
            position = str(place)
            announcement = announcement + f" {position}. " + queue[i]

        print(announcement)

def take_a_number(queue, name):
    position = str(1 + len(queue))
    print(f"Welcome, {name}. You are number {position} in line.")
    queue.append(name)

def now_serving(queue):
    if len(queue) == 0:
        print('There is nobody waiting to be served!')
    else:
        print(f"Currently serving {queue[0]}.")
        queue.pop(0)

    