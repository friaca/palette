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

```python pallete.py -i input [-c | --colors N] [-s | --with-source] -o output```

- -c --colors: Defines the number of colors the palette will have, the default is 5.

- -s --with-source: If present, the output image will contain the source image