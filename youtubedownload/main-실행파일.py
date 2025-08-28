import configparser
from AudioDownload import AudioDownload
from ConvertmpFile import ConvertmpFile
from VideoDownload import VideoDownload

# config.ini 읽기
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

VIDEO_URLS = [url.strip() for url in config.get('VIDEO', 'urls').splitlines() if url.strip()]
AUDIO_URLS = [url.strip() for url in config.get('AUDIO', 'urls').splitlines() if url.strip()]
print(VIDEO_URLS)
print(AUDIO_URLS)


def download_video():
    if not VIDEO_URLS:
        print("VIDEO URL이 설정되지 않았습니다.")
        return
    for sUrl in VIDEO_URLS:
        sUrl = sUrl.strip()  # 앞뒤 공백 제거
        download = VideoDownload(sUrl)
        sName, sPath = download.getDownload()
        print(f"Video downloaded: {sName}, Path: {sPath}")


def download_audio():
    if not AUDIO_URLS:
        print("AUDIO URL이 설정되지 않았습니다.")
        return
    for sUrl in AUDIO_URLS:
        sUrl = sUrl.strip()  # 앞뒤 공백 제거
        download = AudioDownload(sUrl)
        sName, sPath = download.getDownload()
        print(f"Audio downloaded: {sName}, Path: {sPath}")


def convert_files():
    convert = ConvertmpFile()
    convert.convert_all()
    print("All files converted.")


if __name__ == '__main__':
    download_audio()

# 실행파일 만들기
# pyinstaller --onefile --name convert_files main.py -- --convert
# pyinstaller --onefile --name download_video main.py -- --video
# pyinstaller --onefile --name download_audio main.py -- --audio