import sys
from parse import parse_line, parse_args
from helper import run_command, print_help
# from PIL import Image

def main():
  parse_args(sys.argv)
  return
  imagick_output = run_command('magick convert group_less.jpg -format %c -depth 8 histogram:info:-', get_output=True)
  output_lines = imagick_output.split('\n')
  parsed_lines = [parse_line(line) for line in output_lines]
  sorted_lines = sorted(parsed_lines, key=lambda l: int(l['frequency']), reverse=True)
  # image = Image.new("RGB", (1000, 1000), "#FF0000")

  for color in sorted_lines:
    print(color)
  # image.show()





if __name__ == '__main__':
  main()