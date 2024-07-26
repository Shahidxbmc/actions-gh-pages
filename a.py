from pytubefix import YouTube

url="https://m.youtube.com/watch?v=bNyUyrR0PHo"
yt = YouTube(url)
#stream = print(yt.streams.get_highest_resolution()
print(yt.streams.all()[0].url)



       
