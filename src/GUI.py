from tkinter import *
import tkinter.font

from youtube_download import download

projectTitle = 'Youtube Downloader v1.0'

# 사용 색상
bgcolor = '#F2F0EB'
btncolor = '#FF0000'

# 창 생성
root = Tk()
# 프로그램 크기 및 위치 지정
root.geometry("440x400+500+150")
#프로그램 창 크기 변경 제한
root.resizable(False, False)
# 프로그램 상단 타이틀 바 로고 import
root.iconphoto(False, PhotoImage(file='./image/youtube.png'))
# 프로그램 배경 설정
root.configure(bg=bgcolor)
# 프로그램 상단 타이틀 바 명칭 설정
root.title("유튜브 다운로드 프로그램")

# 폰트 설정
font = tkinter.font.Font(family="KoPubWorld돋움체 Medium",
                         size=15, weight=tkinter.font.BOLD)  # 버튼 폰트
font0 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=1)  # 공백 폰트
font1 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=11)  # 설명 폰트
font2 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=18)  # TEXT 박스
font25 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=25)  # 공백 폰트
font3 = tkinter.font.Font(family="KoPubWorld돋움체 Medium",
                          size=18, weight=tkinter.font.BOLD)  # Title 폰트
# 메인 로고 import
image1 = PhotoImage(file="./image/youtube.png")
# 로고 사이즈 조절
photoimage1 = image1.subsample(6, 6)
# 로고를 라벨로 설정
imgLabel1 = Label(root, image=photoimage1, width=85,
                  height=85, background=bgcolor)

# 버튼 설정
btn = Button(root, text="동영상 다운로드", width=24, height=1, font=font,
              foreground='white', background=btncolor, command=lambda: download(inputText.get()))


# 공백 설정
label000 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font25, background=bgcolor)
label001 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font0, background=bgcolor)
label002 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font0, background=bgcolor)
label003 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font0, background=bgcolor)

# 프로그램명 설정
systemTitle = Label(root, text=projectTitle, anchor="center",
                    width=40, height=1, font=font3, background=bgcolor, fg='#2f3640')
# 설명 입력
label2 = Label(root, text='[링크] Youtube 공유 링크를 넣어주세요.', anchor="sw",
               width=40, height=1, font=font1, background=bgcolor, padx=100)
# 텍스트 박스 설정
inputText = Entry(root, width=35, font=font1,
                  background='azure', relief='solid')

# 공백
label000.pack()
# 메인로고
imgLabel1.pack()
# 공백
label001.pack()
# 프로그램명
systemTitle.pack()
# 공백
label002.pack()
# 설명
label2.pack()
# 텍스트 박스
inputText.pack()
# 공백
label003.pack()
# 버튼
btn.pack()

# 'Enter' 키를 눌러 '동영상 다운로드' 버튼 클릭
root.bind('<Return>', lambda event=None: btn.invoke())
root.mainloop()
