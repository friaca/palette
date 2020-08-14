import re
import argparse

def parse_line(line):
  # 72469: (127,255,127) #7FFF7F srgb(127,255,127)
  regex = r'(\d+): (\(.+\)) (#[0-9A-F]+) (\w+)(.+){0,1}'
  match = re.search(regex, line)
  parsed_line = { 'frequency': match.group(1), 'rgb': match.group(2), 'hex': match.group(3) }

  return parsed_line

def parse_args():
  parser = argparse.ArgumentParser(description='Generate a color palette based on a source image')
  parser.add_argument('-i', '--input', dest='input', type=str, help='input file', required=True)
  parser.add_argument('-c', '--colors', dest='colors', type=int, help='number of colors of palette', default=5)
  parser.add_argument('-s', '--with-source', dest='source', help='save the palette with the source image', action='store_true')
  parser.add_argument('-v', '--value', dest='value', help='includes the color hex code in the image', action='store_true')
  parser.add_argument('-o', '--output', dest='output', type=str, help='output path', required=True)

  arguments = parser.parse_args()
  return arguments