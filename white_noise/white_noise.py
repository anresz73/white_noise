#!white_noise_env/bin/python3
# -*- coding: utf-8 -*-
#
# Created on 2022/02/22
#
# Dead Channel Generator
#/
# /https://github.com/anresz73/white_noise

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create numpy random matrix with photo pixel data 
h, au = 400, (1. + 5. ** .5) / 2.
white_noise_image = np.random.randint(low = 10, high = 245, size = (h, int(h * au), 3, 10))

# Initialize Figure
fig, ax = plt.subplots()
ax.axis('off')

# Frame Gen Function
def func(frame):
  return ax.imshow(white_noise_image[:, :, :, frame])

#FuncAnimation from matplotlib
anim = FuncAnimation(
    fig = fig,
    func = func,
    frames = 10,
    cache_frame_data = False
)

#Save gif
anim.save('./animation.gif', writer='pillow', fps=60)