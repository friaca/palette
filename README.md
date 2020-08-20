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

```python pallete.py -i input [options...] -o output```

| Argument | Abbrev. | Default | Description |
| ---    | ---     | ---     | ---         |
| --colors| -c     | 5       | Number of dominant colors to return |
| --add-source | -s | `False` | (Not working for now) If present, the output image will contain the source image |
| --values | -v    | `False` | Includes the hex value in every color block (invalid if `-p` is present) |
| --percentage | -p  | `False` | Instead of color blocks of equal widths, the blocks' width is equivalent to the color's frequency |