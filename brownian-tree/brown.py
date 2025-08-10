import numpy as np
import matplotlib.pyplot as plt
import random
import math

GRID_SIZE = 801      
MAX_PARTICLES = 10000 
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
center = GRID_SIZE // 2
grid[center, center] = 1

max_radius = 1.0
spawn_radius = 10.0
kill_radius = 20.0

print("Optimized simulation starting...")

for i in range(MAX_PARTICLES):
    
    angle = 2 * math.pi * random.random()
    x = int(center + spawn_radius * math.cos(angle))
    y = int(center + spawn_radius * math.sin(angle))
    walker_pos = [x, y]

    while True:
        step_x = random.randint(-1, 1)
        step_y = random.randint(-1, 1)
        if step_x == 0 and step_y == 0:
            continue
            
        walker_pos[0] += step_x
        walker_pos[1] += step_y
        
        walker_pos[0] = np.clip(walker_pos[0], 0, GRID_SIZE - 1)
        walker_pos[1] = np.clip(walker_pos[1], 0, GRID_SIZE - 1)
        
        x, y = walker_pos[0], walker_pos[1]

        dist_from_center = math.sqrt((x - center)**2 + (y - center)**2)
        if dist_from_center > kill_radius:
            break

        stuck = False
        for nx in range(max(0, x - 1), min(GRID_SIZE, x + 2)):
            for ny in range(max(0, y - 1), min(GRID_SIZE, y + 2)):
                if grid[nx, ny] == 1:
                    grid[x, y] = 1
                    stuck = True
                    
                    max_radius = max(max_radius, dist_from_center)
                    spawn_radius = max_radius + 10
                    kill_radius = max_radius + 50 
                    break
            if stuck:
                break
        
        if stuck:
            if (i + 1) % 100 == 0:
                 print(f"Particle {i+1}/{MAX_PARTICLES} attached. New max radius: {max_radius:.1f}")
            break

print("Simulation finished. Generating plot...")
plt.figure(figsize=(12, 12))
plt.imshow(grid, cmap='afmhot_r') 
plt.title(f"Optimized Brownian Tree ({MAX_PARTICLES} particles)")
plt.axis('off')
plt.show()