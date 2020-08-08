def quantitize_image(filename):
  try:
    run_command(f'magick {filename} -kmeans 5 {filename}_temp.png')
  except:
    print('Something went wrong')
