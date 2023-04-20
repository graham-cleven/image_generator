import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_geometric_image(filename='geometric_image.png'):
    # Create a figure
    fig = plt.figure()

    # Create 3D axes
    ax = fig.add_subplot(111, projection='3d')

    # Define vertices of the cuboid
    vertices = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 1]
    ]

    # Define the edges connecting the vertices
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7],
        [4, 5],
        [5, 6],
        [6, 7],
        [7, 4]
    ]

    # Plot the cuboid using vertices and edges
    for edge in edges:
        ax.plot3D(*zip(*[vertices[edge[0]], vertices[edge[1]]]), color='#6c63ff')

    # Remove grid lines
    ax.grid(False)

    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Set background color
    ax.set_facecolor('white')
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

    # Set the aspect ratio of the plot
    ax.set_box_aspect((1, 1, 1))

    # Save the image
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')

    # Show the plot
    plt.show()

# Generate the image
generate_geometric_image()

