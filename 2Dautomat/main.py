import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid_size = (50, 50)
grid = np.zeros(grid_size)

initial_population = 0.2
random_indices = np.random.choice(np.prod(grid_size), size=int(initial_population * np.prod(grid_size)), replace=False)
grid.ravel()[random_indices] = 1

# game rules
def apply_rules(grid):
    neighbor_count = sum(np.roll(np.roll(grid, i, axis=0), j, axis=1) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i != 0 or j != 0)) #zadnji pogoj preprecuje da bi upostevali trenutno celico kot sosednjo
    new_grid = np.logical_or(np.logical_and(grid == 1, neighbor_count == 2), neighbor_count == 3)
    return new_grid.astype(int)

def update_grid(frameNum, img, grid): 
    new_grid = apply_rules(grid) 
    img.set_data(new_grid) 
    grid[:] = new_grid[:] 
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary', interpolation='nearest') 
ani = animation.FuncAnimation(fig, update_grid, fargs=(img, grid), frames=100, interval=50, save_count=50) 


def on_click(event):
    x, y = int(event.xdata), int(event.ydata)
    grid[y, x] = 1 - grid[y, x]
    img.set_data(grid)
    fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
