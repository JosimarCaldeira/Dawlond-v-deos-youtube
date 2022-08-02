from pytube import YouTube, streams
from pytube.cli import on_progress
link= input("Insira o link para dawlond:")
youtube=YouTube(link,on_progress_callback= on_progress)
print("Titulo", youtube.title)
print ("Baixando")
coleta=youtube.streams.get_highest_resolution()
coleta.download()
