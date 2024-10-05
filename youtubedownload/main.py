from AudioDownload import AudioDownload
from VideoDownload import VideoDownload


def download_video():
    sUrl = 'https://www.youtube.com/watch?v=rWCY5L77Mz8'
    download = VideoDownload(sUrl)
    sName, sPath = download.getDownload()
    # print(sName)
    # print(sPath)


def download_audio():
    sUrl = 'https://www.youtube.com/watch?v=09R8_2nJtjg'
    download = AudioDownload(sUrl)
    sName, sPath = download.getDownload()
    print(sName)
    print(sPath)


if __name__ == '__main__':
    download_video()
    download_audio()
