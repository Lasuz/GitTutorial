import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

text = ax.text(0.5, 0.5, '', ha='center', va='center', fontsize=100, color='blue')

# Change the figure background color
fig.patch.set_facecolor('black')

# Change the axes background color
ax.set_facecolor('yellow')


# Initialize the text to be empty
def init():
    text.set_text('')
    return text,

# Update the frame
def update(frame):
    if frame < 10:
        text.set_text('')
    else:
        text.set_text('\U0001F600')
    return text,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 20), init_func=init, blit=True)

plt.show()

'''
1) Change Text 
2) Frequency
3) Text Color
4) Background Color
 
'''