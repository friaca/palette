import sys
from helper import run_command, delete_file
from parse import parse_line, parse_args
from colorspaces import quantitize_image, generate_histogram
from image import without_source

def main():
  arguments = parse_args()
  filename, extension = arguments.input.rsplit('.', 1)
  temp_file = f'{filename}_temp.png'

  try:
    quantitize_image(filename, extension, arguments.colors)
    imagick_output = generate_histogram(temp_file) 
    delete_file(temp_file)
  except:
    print('Something went wrong with ImageMagick, is it installed correctly? Its version needs to be at least 7.0.9')
  else:
    output_lines = imagick_output.split('\n')
    parsed_colors = [parse_line(line) for line in output_lines]
    sorted_colors = sorted(parsed_colors, key=lambda l: int(l['frequency']), reverse=True)

    size = None
    image = None
    
    if arguments.source:
      pass
    else:
      size = 1000 if arguments.colors < 6 else arguments.colors * 200
      image = without_source(size, arguments.colors, arguments.value, sorted_colors)

    try:
      output, extension = arguments.output.rsplit('.', 1)
      image.save(f'{output}_palette.{extension}')
    except OSError as oserror:
      print(f'Couldn\'t save the image for some reason\n{oserrror.strerror}') 

if __name__ == '__main__':
  main()