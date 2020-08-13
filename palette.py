import sys
from helper import run_command, delete_file
from parse import parse_line, parse_args
from colorspaces import quantitize_image, generate_histogram

try:
  from PIL import Image
except ImportError:
  print('Couldn\'t import Pillow, please intall it to use palette')

def main():
  arguments = parse_args()
  filename, extension = arguments.input.rsplit('.', 1)
  temp_file = f'{filename}_temp.png'

  try:
    quantitize_image(filename, extension, arguments.colors)
    imagick_output = generate_histogram(temp_file) 
    delete_file(temp_file)
  except:
    print('Something went wrong with ImageMagick, is it installed correctly?')
  else:
    output_lines = imagick_output.split('\n')
    parsed_colors = [parse_line(line) for line in output_lines]
    sorted_colors = sorted(parsed_colors, key=lambda l: int(l['frequency']), reverse=True)

    size = 1000 if arguments.colors < 6 else arguments.colors * 200 
    image = Image.new("RGB", (size, size), "#FFFFFF")

    for i in range(len(sorted_colors)):
      initialX = (size // arguments.colors) * i
      finalX = (size //  arguments.colors) * (i + 1)
      image.paste(sorted_colors[i]['hex'], [initialX, 0, finalX, size])

    image.show()

if __name__ == '__main__':
  main()