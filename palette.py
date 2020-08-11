import sys
from helper import run_command
from parse import parse_line, parse_args
from colorspaces import quantitize_image, generate_histogram
# from PIL import Image

def main():
  arguments = parse_args()
  filename, extension = arguments.input.rsplit('.', 1)

  quantitize_image(filename, extension, arguments.colors)
  imagick_output = generate_histogram(f'{filename}_temp.png')

  output_lines = imagick_output.split('\n')
  parsed_lines = [parse_line(line) for line in output_lines]
  sorted_lines = sorted(parsed_lines, key=lambda l: int(l['frequency']), reverse=True)
  # image = Image.new("RGB", (1000, 1000), "#FF0000")

  for line in sorted_lines:
    print(line)
  # image.show()





if __name__ == '__main__':
  main()