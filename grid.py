import os
from animal import Animal

def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED: {todo} >>>')

grid = [[0] * 20 for i in range(20)]
for a in grid:
    print(a)

input('some input')
os.system('clear')

i = 0


print("    ", end="")

while i < 9:
    print(f" {i+1}  ", end="")
    i += 1

while i < 20:
    print(f" {i+1} ", end="")
    i += 1

print("")
i = 0

print("    ", end="")

while i < 20:
    print("____", end="")
    i += 1

print("")

i = 1

for a in grid:
    if i < 10:
        print(f"{i}  |", end="")
    else:
        print(f"{i} |", end="")

    for b in a:
        print(f" {b}  ", end="")

    print("")
    i += 1

def move(self, direction='right'):
        print(f'moving to {direction}. ')
        self.x += 1
        


def header():
    i = 0
    
    print("    ", end="")

    while i < 9:
        print(f" {i+1}  ", end="")
        i += 1

    while i < 20:
        print(f" {i+1} ", end="")
        i += 1

    print("")
    i = 0

    print("    ", end="")

    while i < 20:
        print("____", end="")
        i += 1

    print("")



class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.grid = [['.' for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.zebras = [Animal(0, 0) for _ in range(num_zebras)]
        self.lions = [Animal(0, 0) for _ in range(num_lions)]
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}') 
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')