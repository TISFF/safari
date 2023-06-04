import random

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
        self.hp = 3
    
    def move_to(self, grid, target):
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            grid[self.x][self.y] = Empty(self.x, self.y)
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            grid[self.x][self.y].hp = 0
            grid[self.x][self.y] = self
            return True
        else:
            return False

    def  get_neighbors(self, grid, target):
        height = len(grid)
        width = len(grid[0])
        x = self.x
        y = self.y
        neighbors = []
        neighbors.append([x - 1, y])
        neighbors.append([x + 1, y])
        neighbors.append([x, y - 1])
        neighbors.append([x, y + 1])

        neighbors_able = []
        for neighbor in neighbors:
            if (neighbor[0] >=  0 and neighbor[0] < height
                and neighbor[1] >= 0 and neighbor[1] < width
                and str(grid[neighbor[0]][neighbor[1]]) == target):
                neighbors_able.append(neighbor)
        
        return neighbors_able

    def breed(self, grid):
        child = self.__class__(self.x, self.y)
        child.move_to(grid, target = '.')
        grid[self.x][self.y] = self

class Empty(Animal):
    def __str__(self):
        return '.'
    
class Zebra(Animal):
    def __str__(self):
        return 'Z'
    
    def move(self, grid):
        self.move_to(grid, target = '.')
    
    def ready_to_breed(self):
        if (self.age > 0 and self.age % 3 == 0):
            return True
        return False

class Lion(Animal):
    def __str__(self):
        return 'L'

    def move(self, grid):
        successful = self.move_to(grid, target = 'Z')
        if (successful == True):
            self.hp = 3
        else:
            self.move_to(grid, target = '.')
            self.hp -= 1

    def ready_to_breed(self):
        if (self.age > 0 and self.age % 8 == 0):
            return True
        return False