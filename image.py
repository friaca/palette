from colorspaces import get_contrasting_color, get_color_indices

try:
  from PIL import Image, ImageFont, ImageDraw
except ImportError:
  print('Couldn\'t import Pillow, please intall it to use palette')


def generate_palette(color_list, show_values, by_percentage):
  size = 1000 if len(color_list) < 6 else len(color_list) * 200
  new_image = Image.new("RGB", (size, size), "#FFFFFF")
  color_indices = get_color_indices(color_list, size, by_percentage)
  n_color = len(color_indices)

  for i in range(len(color_indices)):
    new_image.paste(color_indices[i]['hex'], [color_indices[i]['start'], 0, color_indices[i]['end'], size])

  if show_values and not by_percentage:
    drawing = ImageDraw.Draw(new_image)
    font = ImageFont.truetype("arial", 30)

    for i in range(n_color):
      fill = get_contrasting_color(color_list[i]['hex'])
      x = ((size // n_color) * i) + 30
      
      drawing.text((x, size - 75), color_list[i]['hex'], font=font, fill=fill)

  return new_image