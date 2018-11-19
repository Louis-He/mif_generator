# sound2mif [![](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-371/)

## Introduction
convert sound file to mid for FPGA

You can convert sound track to .mif file.

Supported file format:
.m4a, .mp3, .wav, .raw

## Notice:
1. you need depedency package: wave, pydub
2. Only tested on python 3.7 but it should work on all python3 versions.

## usage
1. run the following inside the directory of main.py.

```Bash
python3 main.py
```

**Common Error**: ImportError: `No module named wave` or `No module named pydub`

**Solution**: run 
```Bash
sudo pip3 install -r requirements.txt
```

2. Example of execuating
```
FileName: sample.m4a
Need to cut the sound track:(y? stay blank if not) y
initial:(ms) 0
final:(ms) 10000
original frame rate of sound track: 44100 Hz
Set new frame rate:(Hz) 6000 
[INFO] Exporting sample_out.wav
[INFO] wav params is : _wave_params(nchannels=1, sampwidth=1, framerate=6000, nframes=60000, comptype='NONE', compname='not compressed')
[INFO] Converting sample_out.wav to mif
sample.m4a convert to sample.mif COMPLETE.
---------------------------
```
