import os.path
from pytubefix import YouTube


def getFolder():
    folder = os.path.join(os.getcwd(), 'down')
    os.makedirs(folder, exist_ok=True)
    return folder


class VideoDownload:
    def __init__(self, sUrl):
        self.sUrl = sUrl
        self.yt = YouTube(self.sUrl)

    def getDownload(self):
        stream = self.yt.streams.get_highest_resolution()
        sPath = stream.download(output_path=getFolder())
        sName = os.path.basename(sPath)
        print(f'{sName} 다운로드 완료')
        return sName, sPath
