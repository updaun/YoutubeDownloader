import os
from tkinter import messagebox
from pytube import YouTube
import sys

import pytube.request
pytube.request.default_range_size = 9437184

class Downloader:
        
    def action(self, url):
        
        self.url = url
        download_path = './Downloads'

        # 링크 미입력시
        if self.url == '':
            print('[오류] 링크를 입력해주세요.\n')
            messagebox.showwarning("유튜브 다운로드 프로그램", "링크를 입력해주세요.")
        
        # 링크 입력시    
        else:
            dl = Downloader()
            # 폴더 생성 함수 호출
            dl.createFolder(download_path)
            # 유튜브 동영상 다운로드 함수 호출
            dl.youtube_download(self.url)


    # 다운로드 폴더 생성 함수
    def createFolder(self, directory):
        try:
            if not os.path.exists(directory):
                # 폴더 생성 메서드
                os.makedirs(directory)
        except Exception as all_e: 
            # 에러 발생시
            print('[오류] 폴더 생성을 실패하였습니다.\n' + directory)
            print('[에러코드]', type(all_e))
            print('[에러내용]', all_e,"\n")
            messagebox.showwarning("유튜브 다운로드 프로그램", "[오류] 폴더 생성을 실패하였습니다.")


    def show_progress_bar(stream, _chunk, _file_handle, bytes_remaining):
        current = ((stream.filesize - bytes_remaining)/stream.filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()

    # 유튜브 동영상 다운로드 함수 
    def youtube_download(self, youtube_url):

        global file_size

        print('[진행] 동영상 다운로드를 시작합니다.\n')

        try:
            # 동영상 다운로드 메서드
            video = YouTube(youtube_url, on_progress_callback=self.show_progress_bar)
            video.register_on_progress_callback(self.show_progress_bar)
            video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()
            video_type.download('./Downloads/')
        
        except Exception as all_e:
            print('[오류] 링크 주소를 다시 확인해 주세요.\n')
            print('[에러코드]', type(all_e))
            print('[에러내용]', all_e,"\n")
            messagebox.showinfo(
            "유튜브 다운로드 프로그램", "[오류] 링크 주소를 다시 확인해 주세요.")

        file_size = video_type.filesize
        print("동영상 용량 :", round(file_size/1000000, 2),"MB\n")

        print('[완료] 동영상을 성공적으로 다운로드 되었습니다.\n')
        messagebox.showinfo(
        "유튜브 다운로드 프로그램", "동영상이 성공적으로 다운로드 되었습니다.")

# test code
with open('./test_url.txt', 'r') as file_data:
    for line in file_data:
        print(line)
        test_url = line
        
dl = Downloader()
dl.youtube_download(test_url)