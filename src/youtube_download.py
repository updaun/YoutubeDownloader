import os
from tkinter import messagebox
from pytube import YouTube

def download(path):
    # 링크 미입력시
    if path == '':
        print('[오류] 링크를 입력해주세요.\n')
        messagebox.showwarning("유튜브 다운로드 프로그램", "링크를 입력해주세요.")
    # 링크 입력시    
    else:
        # 다운로드 폴더 생성 함수
        def createFolder(directory):
            try:
                if not os.path.exists(directory):
                    # 폴더 생성 메서드
                    os.makedirs(directory)
            except OSError: 
                # 에러 발생시
                print('[오류] 폴더 생성을 실패하였습니다.\n' + directory)
                messagebox.showwarning("유튜브 다운로드 프로그램", "[오류] 폴더 생성을 실패하였습니다.")
                
        # 폴더 생성 함수 호출
        createFolder('./Downloads')
        
        # 유튜브 동영상 다운로드 함수 
        def youtube_download(youtube_path):
            # 동영상 다운로드 메서드
            YouTube(youtube_path).streams.first().download('./Downloads/')
            messagebox.showinfo(
            "유튜브 다운로드 프로그램", "동영상이 성공적으로 다운로드 되었습니다.")

        # 유튜브 동영상 다운로드 함수 호출
        youtube_download(path)
        
