import subprocess

def print_help():
  print("""
  Usage: pallete input [...options] output

  Options:
   
  Flag              Default   Description
  --with-source -s: False     saves the pallete with the source image
  --colors -c:      5         Number of colors in the pallete
  """)


def run_command(cmd, get_output = False):
  sanitized_cmd = cmd.strip().split(' ')
  output = subprocess.run(sanitized_cmd, stdout=subprocess.PIPE).stdout.decode('utf8').strip()

  return output if get_output else None