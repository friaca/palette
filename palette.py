import sys
from helper import run_command, delete_file
from parse import parse_line, parse_args
from colorspaces import quantitize_image, generate_histogram
# from PIL import Image

def main():
  arguments = parse_args()
  filename, extension = arguments.input.rsplit('.', 1)
  temp_file = f'{filename}_temp.png'

  try:
    quantitize_image(filename, extension, arguments.colors)
    imagick_output = generate_histogram(temp_file)
    delete_file(temp_file)
  except Exception:
    print('Something went wrong')
  else:
    output_lines = imagick_output.split('\n')
    parsed_lines = [parse_line(line) for line in output_lines]
    sorted_lines = sorted(parsed_lines, key=lambda l: int(l['frequency']), reverse=True)
    # image = Image.new("RGB", (1000, 1000), "#FF0000")

    for line in sorted_lines:
      print(line)

if __name__ == '__main__':
  main()