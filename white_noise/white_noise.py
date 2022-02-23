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

def white_noise(
  h = 200,
  iframes = 10,
  animation_name = 'animation'):
  # Create numpy random matrix with photo pixel data 
  au = (1. + 5. ** .5) / 2.
  white_noise_image = np.random.randint(low = 10, high = 245, size = (h, int(h * au), 3, iframes))

  # Initialize Figure
  fig, ax = plt.subplots()
  plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
  ax.axis('off')
  ax.margins(0.)
  #ax.spines[['right', 'left']].set_visible(False)

  # Frame Gen Function
  def func(frame):
    return ax.imshow(white_noise_image[:, :, :, frame])

  #FuncAnimation from matplotlib
  anim = FuncAnimation(
      fig = fig,
      func = func,
      frames = iframes,
      cache_frame_data = False
  )

  #Save gif
  anim.save(
    f'./{animation_name}.gif',
    writer='pillow',
    fps=60,
    #bbox_inches='tight',
    #savefig_kwargs = {'pad_inches' : 0.,
    #                  'bbox_inches' : 'tight'}
    )