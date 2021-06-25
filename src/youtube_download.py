import os
from tkinter import messagebox
from pytube import YouTube

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

    # 유튜브 동영상 다운로드 함수 
    def youtube_download(self, youtube_url):
            try:
                # 동영상 다운로드 메서드
                YouTube(youtube_url).streams.first().download('./Downloads/')
                print('[완료] 동영상을 성공적으로 다운로드 되었습니다.\n')
                messagebox.showinfo(
                "유튜브 다운로드 프로그램", "동영상이 성공적으로 다운로드 되었습니다.")
            except Exception as all_e:
                print('[오류] 링크 주소를 다시 확인해 주세요.\n')
                print('[에러코드]', type(all_e))
                print('[에러내용]', all_e,"\n")
                messagebox.showinfo(
                "유튜브 다운로드 프로그램", "[오류] 링크 주소를 다시 확인해 주세요.")