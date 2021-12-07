from pytube import YouTube
from os import path

link = input('Enter Video URL: ')

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, file_extension = "mp4").get_highest_resolution().download(output_path = path.join(path.dirname(__file__), "Videos"), filename = input("FileName (include .mp4): "))
except:
    print("Some Error!")
print('Task Completed!')
input('Press any key to exit...')
