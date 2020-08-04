import re
import subprocess
from typing import Optional

def run_command(cmd: str, get_output: Optional[bool] = False):
  sanitized_cmd: [str] = cmd.strip().split(' ')
  output: str = subprocess.run(sanitized_cmd, stdout=subprocess.PIPE).stdout.decode('utf8').strip()

  return output if get_output else None

def parse_line(line: str):
  # 72469: (127,255,127) #7FFF7F srgb(127,255,127)
  regex = r'(\d+): (\(.+\)) (#[0-9A-F]+) (\w+)(.+){0,1}'
  match = re.search(regex, line)
  parsed_line = { 'frequency': match.group(1), 'rgb': match.group(2), 'hex': match.group(3) }

  return parsed_line

def main():
  # run_command('convert tiger.jpg +dither -posterize 3 tiger_min.jpg')
  imagick_output = run_command('convert group_less.jpg -format %c -depth 4 histogram:info:-', get_output=True)
  output_lines = imagick_output.split('\n')
  parsed_lines = [parse_line(line) for line in output_lines]
  sorted_lines = sorted(parsed_lines, key=lambda l: int(l['frequency']), reverse=True)[:20]

  for line in sorted_lines:
    print(line['srgb'])



if __name__ == '__main__':
  main()