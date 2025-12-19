#!/usr/bin/env python3
"""
Fractal Viewer - Mandelbrot Set Generator
Generates and displays a beautiful Mandelbrot set fractal using matplotlib.

The Mandelbrot set is a famous fractal defined by iterating the equation:
z(n+1) = z(n)^2 + c

Where c is a complex number representing each pixel in the complex plane.
Points that remain bounded after many iterations are part of the set.

Requirements:
    pip install matplotlib numpy

Usage:
    python3 fractal_viewer.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def mandelbrot(c, max_iter=100):
    """
    Calculate whether a complex number c is in the Mandelbrot set.

    Args:
        c: Complex number to test
        max_iter: Maximum number of iterations to test

    Returns:
        Number of iterations before divergence (or max_iter if bounded)
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter


def generate_mandelbrot(width=800, height=600, x_min=-2.5, x_max=1.0,
                       y_min=-1.25, y_max=1.25, max_iter=100):
    """
    Generate a Mandelbrot set image as a 2D array.

    Args:
        width: Image width in pixels
        height: Image height in pixels
        x_min, x_max: Real axis bounds
        y_min, y_max: Imaginary axis bounds
        max_iter: Maximum iterations for each point

    Returns:
        2D numpy array with iteration counts for each pixel
    """
    # Create coordinate arrays
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    # Initialize result array
    mandelbrot_set = np.zeros((height, width))

    # Calculate Mandelbrot set for each pixel
    print("Generating Mandelbrot set...")
    for i in range(height):
        # Show progress every 50 rows
        if i % 50 == 0:
            print(f"Progress: {i}/{height} rows ({100*i//height}%)")

        for j in range(width):
            # Convert pixel coordinates to complex number
            c = complex(x[j], y[i])
            # Calculate iterations for this point
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)

    print("Generation complete!")
    return mandelbrot_set


def create_custom_colormap():
    """
    Create a beautiful custom colormap for the fractal.

    Returns:
        Custom matplotlib colormap
    """
    # Define colors: deep blue -> cyan -> yellow -> red -> black
    colors = ['#000033', '#0066cc', '#00cccc', '#ffff00', '#ff6600', '#000000']
    n_bins = 256
    cmap = LinearSegmentedColormap.from_list('mandelbrot', colors, N=n_bins)
    return cmap


def display_fractal(mandelbrot_set):
    """
    Display the Mandelbrot set using matplotlib.

    Args:
        mandelbrot_set: 2D array of iteration counts
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 9))

    # Create custom colormap
    cmap = create_custom_colormap()

    # Display the fractal
    im = ax.imshow(mandelbrot_set, cmap=cmap, interpolation='bilinear',
                   extent=[-2.5, 1.0, -1.25, 1.25], origin='lower')

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, label='Iterations to divergence')

    # Set labels and title
    ax.set_xlabel('Real axis')
    ax.set_ylabel('Imaginary axis')
    ax.set_title('Mandelbrot Set Fractal', fontsize=16, fontweight='bold')

    # Add grid for reference
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

    # Tight layout for better appearance
    plt.tight_layout()

    print("\nDisplaying fractal...")
    print("Close the window to exit.")

    # Show the plot
    plt.show()


def main():
    """
    Main function to generate and display the Mandelbrot set.
    """
    print("=" * 60)
    print("Mandelbrot Set Fractal Viewer")
    print("=" * 60)
    print()
    print("This script generates a visualization of the Mandelbrot set,")
    print("one of the most famous fractals in mathematics.")
    print()

    # Configuration
    WIDTH = 800
    HEIGHT = 600
    MAX_ITERATIONS = 100

    # Coordinate bounds (complex plane)
    X_MIN, X_MAX = -2.5, 1.0
    Y_MIN, Y_MAX = -1.25, 1.25

    print(f"Configuration:")
    print(f"  Resolution: {WIDTH}x{HEIGHT} pixels")
    print(f"  Max iterations: {MAX_ITERATIONS}")
    print(f"  Real axis: [{X_MIN}, {X_MAX}]")
    print(f"  Imaginary axis: [{Y_MIN}, {Y_MAX}]")
    print()

    # Generate the Mandelbrot set
    mandelbrot_set = generate_mandelbrot(
        width=WIDTH,
        height=HEIGHT,
        x_min=X_MIN,
        x_max=X_MAX,
        y_min=Y_MIN,
        y_max=Y_MAX,
        max_iter=MAX_ITERATIONS
    )

    # Display the fractal
    display_fractal(mandelbrot_set)

    print("\nThank you for using Mandelbrot Set Fractal Viewer!")


if __name__ == "__main__":
    # Check if required libraries are available
    try:
        import numpy
        import matplotlib
    except ImportError as e:
        print("Error: Required libraries not found.")
        print("Please install required packages:")
        print("  pip install matplotlib numpy")
        print(f"\nMissing: {e}")
        exit(1)

    main()
