from colorspaces import get_contrasting_color

try:
  from PIL import Image, ImageFont, ImageDraw
except ImportError:
  print('Couldn\'t import Pillow, please intall it to use palette')

def without_source(size, n_color, with_values, color_list):
  image = Image.new("RGB", (size, size), "#FFFFFF")

  for i in range(len(color_list)):
    initialX = (size // n_color) * i
    finalX = (size //  n_color) * (i + 1)
    image.paste(color_list[i]['hex'], [initialX, 0, finalX, size])

  if with_values:
    drawing = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial", 30)

    for i in range(len(color_list)):
      fill = get_contrasting_color(color_list[i]['hex'])

      x = ((size // n_color) * i) + 30
      drawing.text((x, size - 75), color_list[i]['hex'], font=font, fill=fill)

  return image

# def with_source(source, size, n_color, color_list):
#   image = Image.new("RGB", (size, size), "#FFFFFF")