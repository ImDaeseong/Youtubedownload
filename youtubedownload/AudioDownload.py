import os.path
import re
from pytubefix import YouTube


def getFolder():
    folder = os.path.join(os.getcwd(), 'down')
    os.makedirs(folder, exist_ok=True)
    return folder


def getFileName(sName):
    # 파일 이름에 사용할 수 없는 문자 제거
    return re.sub(r'[\\/*?:"<>|]', "", sName)


class AudioDownload:
    def __init__(self, sUrl):
        self.sUrl = sUrl
        self.yt = YouTube(self.sUrl)

    def getDownload(self):
        try:
            stream = self.yt.streams.filter(only_audio=True).first()

            sTitle = getFileName(self.yt.title)
            sFileName = f"{sTitle}.mp4"

            sPath = stream.download(output_path=getFolder(), filename=sFileName)
            sName = os.path.basename(sPath)
            print(f'{sName} 다운로드 완료')
            return sName, sPath
        except Exception as e:
            print(f'다운로드 error:{str(e)}')
            return None, None
