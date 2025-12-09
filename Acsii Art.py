from PIL import Image
import os
import shutil

def get_terminal_size():
    ter_size = shutil.get_terminal_size(fallback=(80, 24)) 
    if ter_size.columns < ter_size.lines:
        return ter_size.columns
    else:
        return ter_size.lines

# List of characters to use for ASCII art
ASCII_CHARS = "@#%$&WM8BDQKHAXpqdbkhaowmZ0LCJUYcvunxrjft12345679~^*()_+-=[]{}\\|/<>?;:'\",.!` "

# Ask for the path (you can type it or drag the file into the terminal)
path = input("Enter the path to your image file: ").strip()

print("\033c", end="")

# Strip quotes if the OS adds them when dragging into terminal
if (path.startswith('"') and path.endswith('"')) or (path.startswith("'") and path.endswith("'")):
    path = path[1:-1]

if not os.path.isfile(path):
    raise FileNotFoundError(f"File not found: {path}")

# Open the image with Pillow
image = Image.open(path)

# Convert to grayscale
image = image.convert("L")

# Convert to grayscale
image = image.convert("L")

# Resize the image to lower the "resolution" of the ASCII art
# You can adjust new_width to control how wide the output is
new_width = get_terminal_size()
original_width, original_height = get_terminal_size(), get_terminal_size()
aspect_ratio = original_height / original_width
# The 0.5 factor compensates for terminal characters being taller than they are wide
new_height = max(1, int(aspect_ratio * new_width))
image = image.resize((new_width, new_height))

# Set up the table for the ASCII grid
width, height = image.size
grid = [[" " for _ in range(width)] for _ in range(height)]

# Set up the table for the ASCII grid
width, height = image.size
grid = [[" " for _ in range(width)] for _ in range(height)]

# Load the pixels
pixels = image.load()

# Number of characters in our gradient
n = len(ASCII_CHARS)

# Change each pixel to a letter
for y in range(height):
    for x in range(width):
        pixel_value = pixels[x, y]
        # Map gray_value (0–255) to an index (0–n-1)
        index = pixel_value * (n - 1) // 255

        # Pick the character for this pixel
        grid[y][x] = ASCII_CHARS[index]

# Print the ASCII art
for line in grid:
    print(" ".join(line))