import random
from PIL import Image, ImageDraw

# Define image size and taper range
width = 500
height = 700
taper_range = (0.2, 0.8)

# Create a new image
image = Image.new("RGB", (width, height), "#ffffff")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define the color
color = "#6c63ff"

# Draw a series of triangles
for y in range(0, height, 40):
    # Determine the tapering factor for this row
    taper = ((y / height) ** 2) * (taper_range[1] - taper_range[0]) + taper_range[0]
    # Determine the number of triangles to draw in this row
    num_triangles = int((width / 40) * taper)
    # Draw the triangles
    for i in range(num_triangles):
        # Define the vertices of the triangle
        x = i * 40 + random.randint(-10, 10)
        if x < 0 or x + 40 > width:
            continue  # Skip triangles that would be cut off by the edge
        points = [(x, y), (x + 40, y), (x, y + 40)]
        # Randomly rotate the triangle by 0, 90, 180, or 270 degrees
        angle = random.choice([0, 90, 180, 270])
        rotated_points = [(x * (1 - angle // 180) + y * (angle // 90), 
                           y * (1 - angle // 180) - x * (angle // 90)) 
                          for x, y in points]
        # Draw the rotated triangle
        draw.polygon(rotated_points, fill=color, outline=color)

# Save the image
image.save("tapered_minimalist_geometric_image.png")

