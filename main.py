#import os
import wave
#import array
from pydub import *
#from matplotlib import pyplot
print('sound2mif.py now supports file format: .m4a, .mp3, .wav, and .raw')

while True:
    fileName = input('FileName: ')
    type = ""
    isRecognized = False
    if fileName.find('m4a') != -1:
        type = 'm4a'
        isRecognized = True
    elif fileName.find('mp3') != -1:
        type = 'mp3'
        isRecognized = True
    elif fileName.find('wav') != -1:
        type = 'wav'
        isRecognized = True
    elif fileName.find('raw') != -1:
        type = 'raw'
        isRecognized = True
    else:
        print('Error: Cannot recognize the format of the file.')

    if isRecognized:
        try:
            # read in original sound track
            # print(fileName)
            # print(type)
            original_audio_file = AudioSegment.from_file(fileName, type)

            cut = input('Need to cut the sound track:(y? stay blank if not) ')
            if cut.lower() == 'y':
                initial = input('start point:(ms) ')
                final = input('end point:(ms) ')
                initial = int(initial)
                final = int(final)
                original_audio_file = original_audio_file[initial : final]

            print('original frame rate of sound track: ' + str(original_audio_file.frame_rate) + ' Hz')

            original_audio_file = original_audio_file.set_channels(channels=1)
            frameRate = int(input('Set new frame rate:(Hz) '))
            bits = int(input('Set bits width: '))
            try:
                # lower the quality of the sound track
                original_audio_file = original_audio_file.set_frame_rate(frame_rate=frameRate)
                original_audio_file = original_audio_file.set_sample_width(1)

                # export wav standard sound track
                print('[INFO] Exporting ' + fileName[:fileName.find('.')] + "_out.wav")
                original_audio_file.export(fileName[:fileName.find('.')] + "_out.wav", format="wav")

                try:
                    f = wave.open(fileName[:fileName.find('.')] + "_out.wav", 'rb')

                    params = f.getparams()  # get wave file params
                    print("[INFO] wav params is :", params)
                    print('[INFO] Converting ' + fileName[:fileName.find('.')] + "_out.wav to mif")

                    # open a txt file
                    LENGTH = f.getnframes()
                    WIDTH = bits
                    try:
                        fData = open(fileName[:fileName.find('.')] + '.mif', 'w')
                        fData.write('Depth = ' + str(LENGTH) + ';\n')
                        fData.write('Width = ' + str(WIDTH) + ';\n')
                        fData.write('Address_radix=dec;\n')
                        fData.write('Data_radix=dec;\n')
                        fData.write('Content\n')
                        fData.write('BEGIN\n')
                        count = 0

                        # countList = []
                        soundwav = []

                        for i in range(LENGTH):  # read range*16 bytes
                            data = f.readframes(1)
                            ldata = list(data)
                            sdata = str(ldata)
                            #    sdata=sdata.replace('\\x',',')
                            fData.writelines(
                                str(count) + '\t:\t' + str(
                                    int(int(int(sdata[1:-1])) / pow(2, 8.0 - WIDTH))))  # 去掉开头和结尾的无关符号
                            # countList.append(count)
                            # soundwav.append(int(int(int(sdata[1:-1])) / pow(2, 8.0 - WIDTH)))
                            fData.write(";\n")  # 添加逗号和换行
                            count += 1

                        # pyplot.plot(countList, soundwav)
                        # pyplot.show()

                        fData.write('END;')
                        f.close()  # close wave file
                        fData.close()  # close data file
                        print(fileName + ' convert to ' + fileName[:fileName.find('.')] + '.mif COMPLETE.')
                        print('---------------------------\n')
                    except:
                        print("Error: cannot write file: " + fileName + ".mif")
                except:
                    print("Error: cannot read file: " + fileName)
            except:
                print('Error: Frame rate should be integers')
        except:
            print("Error: read in original file FAILED")