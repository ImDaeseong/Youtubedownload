from moviepy.editor import AudioFileClip
import os


def getFolder():
    folder = os.path.join(os.getcwd(), 'down')
    os.makedirs(folder, exist_ok=True)
    return folder


def convert_Mp4_toMp3(inputFile, outputFile):
    try:
        audio = AudioFileClip(inputFile)
        audio.write_audiofile(outputFile)
        audio.close()
        print(f'{inputFile} → MP3 변환 완료')
    except Exception as e:
        print(f'변환 실패: {inputFile} 오류: {str(e)}')


class ConvertmpFile:
    def __init__(self, sFolder=None):
        self.sFolder = sFolder if sFolder is not None else getFolder()

    def convert_all(self):
        for sFile in os.listdir(self.sFolder):
            if sFile.lower().endswith('.mp4'):
                input_file = os.path.join(self.sFolder, sFile)
                output_file = input_file.replace('.mp4', '.mp3')
                convert_Mp4_toMp3(input_file, output_file)
