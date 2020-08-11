from helper import run_command

def quantitize_image(filename, extension, colors):
  try:
    run_command(f'magick {filename}.{extension} -kmeans {colors} {filename}_temp.png')
  except Exception as e:
    print('Something went wrong')

def generate_histogram(filename):
  try:
    return run_command(f'magick convert {filename} -format %c -depth 8 histogram:info:-', get_output=True)
  except Exception as e:
    print('Something went wrong')