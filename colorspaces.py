from helper import run_command, delete_file

def quantitize_image(filename, extension, colors):
  try:
    run_command(f'magick {filename}.{extension} -kmeans {colors} {filename}_temp.png')
  except Exception as e:
    print('Something went wrong')

def generate_histogram(filename):
  try:
    output = run_command(f'magick convert {filename} -format %c -depth 8 histogram:info:-', get_output=True)
    delete_file(filename)

    return output
  except Exception as e:
    print('Something went wrong')