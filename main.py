from pytube import YouTube
import webbrowser

yt = YouTube('https://www.youtube.com/watch?v=49DEB-MAQ_4')

print(yt.title)
#webbrowser.open(yt.thumbnail_url, new=2)
print(yt._author)
#print(yt.description)
print(yt.length)
#convertir length en minutes
print(yt.views)
#print(yt.rating)


#show itag
my_streams = yt.streams.filter(progressive=True)
for streams in my_streams:
    print(f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}")

input_itag = input("Enter itag Value : ")
stream = yt.streams.get_by_itag(input_itag)

#stream.download("Bureau", filename="test", filename_prefix= None, skip_existing=True, timeout=None)
stream.download()