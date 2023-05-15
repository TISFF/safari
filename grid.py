import os

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