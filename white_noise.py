#!white_noise/bin/python3
# -*- coding: utf-8 -*-
#
# Created on 2022/02/22
#
# Dead Channel Generator
#/
# /https://github.com/anresz73/white_noise

# Modules
import numpy as np
import click
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

#Functions and decorators
@click.command()
@click.option('--height', default = 200, help = 'Height')
@click.option('--iframes', default = 10, help = '10')
@click.option('--file_name', default = 'white_noise_animation', help = 'gift file name')
def white_noise(
  height = 200,
  iframes = 10,
  file_name = 'animation'
  ):
  """
  Creates a white noise animated picture.
  Args:
      height (int, optional): Picture height. Defaults to 200.
      iframes (int, optional): Frame number. Defaults to 10.
      file_name (str, optional): Name of picture gif file. Defaults to 'animation'.

  Returns:
      None: creates gif from an animated white noise picture
  """
  # Aureum Proportion for animated picture
  au = 1.6
  white_noise_image = np.random.randint(
    low = 10, high = 245, size = (height, int(height * au), 3, iframes))
  # Initialize Figure
  fig, ax = plt.subplots(figsize = (16, 10))
  fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
  ax.axis('off')

  #FuncAnimation from matplotlib
  anim = FuncAnimation(
      fig = fig,
      func = lambda frame: ax.imshow(white_noise_image[:, :, :, frame]),
      frames = iframes,
      cache_frame_data = False
  )

  #Save gif
  file_name = Path(__file__).resolve().parent / file_name
  anim.save(
    file_name.with_suffix('.gif'),
    writer='pillow',
    fps=60,
    )

if __name__ == '__main__':
    white_noise()