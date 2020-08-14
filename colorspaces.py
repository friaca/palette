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

# https://stackoverflow.com/a/12043228
def get_contrasting_color(hex):
  numbers = hex[1:]

  rgb = int(numbers, 16)
  r = (rgb >> 16) & 0xff
  g = (rgb >> 8) & 0xff
  b = (rgb >> 0) & 0xff

  luma = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)

  return '#FFFFFF' if luma < 128 else '#000000'