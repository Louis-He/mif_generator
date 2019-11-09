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

2. Specify your requirements following input prompts.

3. The program will generate three files: out.mif, out.png, outConvert.png.

4. out.mif: file that you can import to FPGA; out.png: 8bits color text image; outConvert.png: image that compressed to bits of color that you specified.

5. Recommendation of parameters
  * Text: Anything but not too long.
  * Font Size: 10 ~ 25
  * bits: 2 ~ 3 denpends on how big the memory
  
6. Example input:
```
Enter Text: Hello
Font Size(pixel, int): 20
bits(up to 8, int): 2
Background Color R-channel(int[0~255]): 255
Background Color G-channel(int[0~255]): 255
Background Color B-channel(int[0~255]): 255
Background Color R-channel(int[0~255]): 127
Background Color G-channel(int[0~255]): 0
Background Color B-channel(int[0~255]): 0
```

7. Example output:
  * out.mif, out.png, outConvert.png as in the directory.