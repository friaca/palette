import re

def parse_line(line):
  # 72469: (127,255,127) #7FFF7F srgb(127,255,127)
  regex = r'(\d+): (\(.+\)) (#[0-9A-F]+) (\w+)(.+){0,1}'
  match = re.search(regex, line)
  parsed_line = { 'frequency': match.group(1), 'rgb': match.group(2), 'hex': match.group(3) }

  return parsed_line
