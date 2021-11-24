from maze_generators.rnd_dfs import RndDfs
import sys
sys.setrecursionlimit(5000)

def main():
    a = RndDfs(50,50)
    a.rnd_dfs(a.startX, a.startY,1)
    a.draw_plot()


if __name__ == "__main__":
    main()
