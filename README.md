# palette
CLI tool that extracts an image's color palette

## Requirements 

- Python 3
- ImageMagick >= 7.0.9-10

## Installation 

Clone the repository and install the dependencies

```
git clone https://github.com/friaca/palette.git
cd palette
pip install requirements.txt
```

## Usage

```python pallete.py -i input [-c | --colors N] [-s | --with-source]  [-v | --values] -o output```

- -c --colors: Defines the number of colors the palette will have, the default is 5.

- -s --add-source: [Not working for now] If present, the output image will contain the source image

- -v --values: Includes the hex value in every color block

- -p --percentage: Instead of color blocks of equal widths, the blocks width is equivalent to the color's frequency 