from AudioDownload import AudioDownload
from ConvertmpFile import ConvertmpFile
from VideoDownload import VideoDownload


def download_video():
    sUrl = 'https://www.youtube.com/watch?v=_Jkom0p9pAk'
    download = VideoDownload(sUrl)
    sName, sPath = download.getDownload()
    # print(sName)
    # print(sPath)


def download_audio():
    sUrl = 'https://www.youtube.com/watch?v=mCXvMohcfP8&list=RDmCXvMohcfP8&start_radio=1'
    download = AudioDownload(sUrl)
    sName, sPath = download.getDownload()
    print(sName)
    print(sPath)


def convert_files():
    convert = ConvertmpFile()
    convert.convert_all()


if __name__ == '__main__':
    #download_video()
    download_audio()
    #convert_files()
