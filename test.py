from pytube import YouTube
import pytube.request
import sys


def show_progress_bar(stream, _chunk, _file_handle, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

with open('./test_url.txt', 'r') as file_data:
    for line in file_data:
        print(line)
        youtube_url = line

video = YouTube(youtube_url, on_progress_callback=show_progress_bar)
video.register_on_progress_callback(show_progress_bar)
video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()
video_type.download('./Downloads/')

# video.register_on_progress_callback(show_progress_bar)
# yt_obj = YouTube(youtube_url, on_progress_callback = progress_function)
# yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path='./Downloads/')

print('[완료] 동영상을 성공적으로 다운로드 되었습니다.\n')