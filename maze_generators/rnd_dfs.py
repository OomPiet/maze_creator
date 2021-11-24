import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from maze_generators.cell import Cell


class RndDfs:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rnd = random.Random()
        self.startX = self.rnd.randint(0, x - 1)
        self.startY = self.rnd.randint(0, y - 1)
        self.startCell = Cell(self.startX, self.startY)
        self.janie = []
        self.gridPlot = []
        self.grid = np.zeros((x, y))
        self.grid[self.startX, self.startY] = 1
        self.N = 3

    def rnd_dfs(self, x, y, p):
        b = [x - self.N >= 0 and self.grid[x - self.N][y] == 0, y + self.N < self.y and self.grid[x][y + self.N] == 0,
             y - self.N >= 0 and self.grid[x][y - self.N] == 0, x + self.N < self.x and self.grid[x + self.N][y] == 0]
        kk = []
        for i in range(4):
            if b[i]:
                kk.append(i)

        while kk:
            a = self.rnd.choice(kk)
            if a == 0:
                self.grid[x - self.N][y] = p
                self.gridPlot.append(np.array([[x, y], [x - self.N, y]]))
                self.rnd_dfs(x - self.N, y, p+1)
            if a == 1:
                self.grid[x][y + self.N] = p
                self.gridPlot.append(np.array([[x, y], [x, y + self.N]]))
                self.rnd_dfs(x, y + self.N, p+1)
            if a == 2:
                self.grid[x][y - self.N] = p
                self.gridPlot.append(np.array([[x, y], [x, y - self.N]]))
                self.rnd_dfs(x, y - self.N, p+1)
            if a == 3:
                self.grid[x + self.N][y] = p
                self.gridPlot.append(np.array([[x, y], [x + self.N, y]]))
                self.rnd_dfs(x + self.N, y, p+1)
            b = [x - self.N >= 0 and self.grid[x - self.N][y] == 0, y + self.N < self.y and self.grid[x][y + self.N] == 0,
                 y - self.N >= 0 and self.grid[x][y - self.N] == 0, x + self.N < self.x and self.grid[x + self.N][y] == 0]
            kk = []
            for i in range(4):
                if b[i]:
                    kk.append(i)
        return

    def draw_plot(self):

        fig, ax = plt.subplots()
        ax.set_xlim(0, self.x)
        ax.set_ylim(0, self.y)
        ls = LineCollection(self.gridPlot)
        ax.add_collection(ls)
        axcb = fig.colorbar(ls)
        plt.sci(ls)  # This allows interactive changing of the colormap.
        plt.show()
        # x = self.gridPlot[:, 0]
        # y = self.gridPlot[:, 1]
        # plt.plot(x, y)
        # plt.show()
