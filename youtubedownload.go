package main

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
	"regexp"

	"github.com/kkdai/youtube/v2"
)

func getFileName(sTitle string) string {
	re := regexp.MustCompile(`[<>:"/\\|?*]`)
	sValue := re.ReplaceAllString(sTitle, "")
	return sValue
}

// 구조체
type VideoAudio struct {
	client *youtube.Client
}

func (va *VideoAudio) Download(sUrl string) (string, error) {

	video, err := va.client.GetVideo(sUrl)
	if err != nil {
		return "", fmt.Errorf("오류:%v", err)
	}

	// 비디오와 오디오 모두 사용할 수 있는 형식
	formats := video.Formats.WithAudioChannels()
	stream, _, err := va.client.GetStream(video, &formats[0])
	if err != nil {
		return "", fmt.Errorf("오류:%v", err)
	}
	defer stream.Close()

	folder := "down"
	if err := os.MkdirAll(folder, os.ModePerm); err != nil {
		return "", fmt.Errorf("오류:%v", err)
	}

	sTitle := getFileName(video.Title)
	sPath := filepath.Join(folder, fmt.Sprintf("%s.mp4", sTitle))
	file, err := os.Create(sPath)
	if err != nil {
		return "", fmt.Errorf("오류:%v", err)
	}
	defer file.Close()

	if _, err := io.Copy(file, stream); err != nil {
		return "", fmt.Errorf("오류:%v", err)
	}

	return sPath, nil
}

func main() {

	va := &VideoAudio{client: &youtube.Client{}}

	urls := []string{
		"https://www.youtube.com/watch?v=rWCY5L77Mz8",
		"https://www.youtube.com/watch?v=09R8_2nJtjg",
		"https://www.youtube.com/watch?v=QgESPJQ0-6c",
		"https://www.youtube.com/watch?v=Wio4UxxfhmY",
		"https://www.youtube.com/watch?v=q-CwVUL_OPE",
		"https://www.youtube.com/watch?v=HABmvsD_ZMs",
	}

	for _, url := range urls {
		if sPath, err := va.Download(url); err != nil {
			fmt.Printf("%v\n", url, err)
		} else {
			fmt.Printf("%s\n", sPath)
		}
	}
}
