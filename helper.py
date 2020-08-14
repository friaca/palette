import os
import subprocess

def run_command(cmd, get_output = False):
  sanitized_cmd = cmd.strip().split(' ')
  output = subprocess.run(sanitized_cmd, stdout=subprocess.PIPE).stdout.decode('utf8').strip()

  return output if get_output else None

def delete_file(filename):
  try:
    os.remove(filename)
  except OSError as oserrror:
    print(f'Couldn\'t delete the file: {oserrror.filename} - {oserrror.strerror}')