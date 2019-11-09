# word2mif [![](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-371/)

## Introduction
Generate mif file for text.

## Notice:
1. you need dependency packages: PIL(Pillow)
2. Only tested on python 3.7 but it should work on all python3 versions.

## usage
1. Run the following command
```Bash
python3 main.py
```

2. Specify your requirement following input prompts.

3. The program will generate three files: out.mif, out.png, outConvert.png.

4. out.mif: file that you can import to FPGA; out.png: 8bits color text image; outConvert.png: image that compressed to bits of color that you specified.

5. Recommendation of parameters
  * Text: Anything but not too long.
  * Font Size: 10 ~ 25
  * bits: 2 ~ 3 denpends on how big the memory