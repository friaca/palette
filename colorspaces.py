from functools import reduce
from math import ceil
from helper import run_command

def quantitize_image(filename, extension, colors):
  try:
    run_command(f'magick {filename}.{extension} -kmeans {colors} {filename}_temp.png')
  except:
    print('Something went wrong while quantitizing your image')

def generate_histogram(filename):
  try:
    return run_command(f'magick convert {filename} -format %c -depth 8 histogram:info:-', get_output=True)
  except:
    print('Something went wrong while generating the histogram')

def get_color_indices(color_list, size, by_percentage):
  color_indices = []
  n_color = len(color_list)

  if by_percentage:
    frequencies = [int(color['frequency']) for color in color_list]
    sum = reduce(lambda acc, curr: acc + curr, frequencies)

    for i in range(n_color):
      percentage = round((frequencies[i] / sum) * 100, 2)
      start = 0 if i < 1 else color_indices[i - 1]['end']
      end = (percentage * (size // 100)) + start

      color_indices.append({'start': ceil(start), 'end': ceil(end), 'hex': color_list[i]['hex']})
  else:
    for i in range(n_color):
      start = (size // n_color) * i
      end = (size //  n_color) * (i + 1)

      color_indices.append({'start': start, 'end': end, 'hex': color_list[i]['hex']})

  return color_indices


# https://stackoverflow.com/a/12043228
def get_contrasting_color(hex):
  numbers = hex[1:]

  rgb = int(numbers, 16)
  r = (rgb >> 16) & 0xff
  g = (rgb >> 8) & 0xff
  b = (rgb >> 0) & 0xff

  luma = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)

  return '#FFFFFF' if luma < 128 else '#000000'