import time
import os

# Function to clear screen (works for Linux/macOS)
def clear():
    os.system('clear')

# Rotate square frames
frames = [
    "  *  \n * * \n  *  ",
    "   * \n  * *\n *   ",
    "  *  \n * * \n  *  ",
    " *   \n  * *\n   * "
]

# Animation loop
while True:
    for frame in frames:
        clear()  # Clear screen
        print(frame)  # Print current frame
        time.sleep(0.2)  # Delay to create animation effect
        