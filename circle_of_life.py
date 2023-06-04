import os
import random
from animal import Empty, Zebra, Lion


def print_TODO(todo):
    print(f'{todo}')

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.grid = [[Empty(x, y) for x in range(world_size)]
                          for y in range(world_size)]
        zebra_coords, lion_coords = self.get_random_coords(num_zebras, num_lions)
        for x, y in zebra_coords:
            self.grid[x][y] = Zebra(x, y)
        for x, y in lion_coords:
            self.grid[x][y] = Lion(x, y)
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}') 
        print(f'\tnumber of zebras = {num_zebras}')
        print(f'\tnumber of lions = {num_lions}')
    
    def get_random_coords(self, num_zebras, num_lions):
        all_coords = [(x, y) for  x in range(self.world_size)
                       for y in range(self.world_size)]
        zebra_coords = random.sample(all_coords, num_zebras)
        all_coords = list(set(all_coords) - set(zebra_coords))
        lion_coords = random.sample(all_coords, num_lions)
        return zebra_coords, lion_coords
    
    def display(self):

        os.system('clear')
        print(f'Clock: {self.timestep}')
        i = 0
        print("    ", end="")

        #print header
        while i < len(self.grid):
            if  i < 9:
                print(f" {i+1}  ", end="")
            elif  i < 20:
                print(f" {i+1} ", end="")
            i += 1

        print("")

        #print lines
        i = 0
        print("    ", end="")
        while i < len(self.grid):
            print("____", end="")
            i += 1

        print("")

        #print lines
        i = 1

        for a in self.grid:
            if i < 10:
                print(f"{i}  |", end="")
            else:
                print(f"{i} |", end="")

            for b in a:
                print(f" {b}  ", end="")

            print("")
            i += 1

        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)]
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)

    def step_breed(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)
                   and animal.ready_to_breed()]
        for animal in animals:
            animal.breed(self.grid)
    
    def housekeeping(self):
        for x, line in enumerate(self.grid):
            for y, animal in enumerate(line):
                if animal.hp == 0:
                    self.grid[x][y] = Empty(x, y)
                else:
                    self.grid[x][y].age += 1

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()
            self.housekeeping()

if __name__ == '__main__':
    safari = CircleOfLife(20, 100, 80)
    safari.display()
    safari.step_move()
    safari.step_breed()
    safari.run()
