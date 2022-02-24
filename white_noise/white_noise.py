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
from matplotlib.animation import FuncAnimation, ArtistAnimation

def white_noise(
  h = 200,
  iframes = 10,
  animation_name = 'animation'):
  # Create numpy random matrix with photo pixel data
  #au = (1. + 5. ** .5) / 2.
  au = 1.6
  white_noise_image = np.random.randint(low = 10, high = 245, size = (h, int(h * au), 3, iframes))

  # Initialize Figure
  fig, ax = plt.subplots(figsize = (16, 10))
  #fig.patch.set_alpha(0.)
  #fig.tight_layout()
  fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
  ax.axis('off')
  #ax.set_ylim(-70, 200)
  #ax.margins(0., 0., tight = True)
  #ax.spines[['right', 'left']].set_visible(False)


  # turn off axis spines
  #ax.xaxis.set_visible(False)
  #ax.yaxis.set_visible(False)
  #ax.set_frame_on(False)

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

  #ArtistAnimation
  #artists = [[ax.imshow(white_noise_image[:, :, :, e], animated = True) for e in range(iframes)]]
  #anim = ArtistAnimation(
  #  fig = fig,
  #  artists = artists
  #)

  #Save gif
  anim.save(
    f'./{animation_name}.gif',
    writer='pillow',
    fps=60,
    #bbox_inches='tight',
    #savefig_kwargs = {'pad_inches' : 0.,
    #}
    )