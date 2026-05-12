"""Task 3.2: Fitting a curve to the 'flame' contour and scaling.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from .composite_curve import composite_bezier, validate_segments
from .scaling import scale_points, plot_scaled_curve

def run_task_3_2():
    # Defining a multi-tongue flame using 6 segments
    flame_segments = [
        ((0.0, 0.0), (-2.0, 1.0), (-2.5, 3.0), (-1.5, 4.0)), # Base to left tongue tip
        ((-1.5, 4.0), (-1.0, 3.0), (-0.8, 3.0), (-0.5, 3.5)), # Left tongue tip to left valley
        ((-0.5, 3.5), (-0.5, 5.0), (-0.2, 7.0), (0.2, 8.0)), # Left valley to main top tip
        ((0.2, 8.0), (0.5, 6.0), (0.8, 4.0), (1.0, 3.5)), # Main top tip to right valley
        ((1.0, 3.5), (1.5, 3.5), (2.0, 4.5), (2.2, 5.0)), # Right valley to right tongue tip
        ((2.2, 5.0), (2.5, 3.0), (1.5, 0.5), (0.0, 0.0)) # Right tongue tip back to base
    ]
    
    if not validate_segments(flame_segments):
        print("Warning: Segments are not properly connected!")
    
    # Generate the base curve (scale 1.0)
    points_base = composite_bezier(flame_segments, n=100)
    
    # Scales from task: 0.5, 1, 1.5, 2
    scales = [0.5, 1.0, 1.5, 2.0]
    center = (0.0, 4.0)  # Approximate center of the flame for aesthetics
    
    # Ensure images directory exists
    output_dir = "images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Generating flame images at scales: {scales}")
    
    for k in scales:
        scaled_points = scale_points(points_base, center, k)
        filename = f"flame_scale_{k}.png"
        filepath = os.path.join(output_dir, filename)
        plot_scaled_curve(scaled_points, k, filepath)
        print(f"Saved: {filepath}")

    # Plot all scales on one graph for comparison
    plt.figure(figsize=(10, 10))
    for k in scales:
        scaled_points = scale_points(points_base, center, k)
        plt.plot(scaled_points[:, 0], scaled_points[:, 1], label=f'Scale {k}')
    
    plt.title('Стилизованное пламя в разных масштабах')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.savefig(os.path.join(output_dir, "flame_all_scales.png"))
    plt.show()

if __name__ == "__main__":
    run_task_3_2()
