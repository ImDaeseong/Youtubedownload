import os

from moviepy.video.io.VideoFileClip import VideoFileClip


def getFolder():
    folder = os.path.join(os.getcwd(), 'down')
    os.makedirs(folder, exist_ok=True)
    return folder


class ConvertmpFile:
    def __init__(self, sFolder=None):
        self.sFolder = sFolder if sFolder is not None else getFolder()

    def convert_Mp4_toMp3(self, inputFile, outputFile):
        try:
            video = VideoFileClip(inputFile)
            audio = video.audio
            audio.write_audiofile(outputFile)
            print(f'{inputFile} 변경 완료')
        except KeyError as e:
            print(f'파일 처리 error:{inputFile} 오류: {str(e)}')
        except Exception as e:
            print(f'변환 실패:{inputFile} 오류: {str(e)}')

    def convert_all(self):
        for sFile in os.listdir(self.sFolder):
            if sFile.endswith('.mp4'):
                input_file = os.path.join(self.sFolder, sFile)
                output_file = input_file.replace('.mp4', '.mp3')
                self.convert_Mp4_toMp3(input_file, output_file)
