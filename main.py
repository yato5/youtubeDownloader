from pytube import YouTube
import webbrowser

link = input("Enter the link of the video: ")
yt = YouTube(link)

#ForEach on all the metadata to present it
def printAllMetadata():
    print("All song(s) used in the video: \n")
    for currentSong in yt.metadata._metadata:
        print("Song : " + currentSong['Song'])
        print("Artist : " + currentSong['Artist'])
        #sometimes, album is missing so to prevent an error, we check if it exists and print warning if not
        print("Album : " + currentSong['Album'] + "\n") if (currentSong.get('Album') != None) else print("Album : No Album \n")

#ForEach on all the keywords to present it
def printAllKeyWord():
    index=0
    print("All keywords of the video: \n")
    for currentKeyWord in yt.keywords:
        print(index, ": " + currentKeyWord)
        index += 1   

#Convert a number of seconds to min + sec
def convertSeconds():
    min = yt.length // 60
    sec = yt.length % 60
    print("The video lasts " + str(min) + "min " + str(sec) + "sec\n")


#If the video is unvailable, we print a warning and exit the program
if(yt.check_availability() != None):
    print("Video is not available")
    exit(0)


#If the user wants to display informations about the video
if(input("Do you want to display informations about " + yt.title + " from " + yt.author + "? (y/n)\n") == "y"):
    printAllKeyWord()
    print("\n")
    convertSeconds()
    print("This video has collected", yt.views, "views\n")
    #If the user wants to display the metadata about the video (can be huge or empty)
    if(input("Do you want to display the metadata about " + yt.title +"? (y/n)\n") == "y"):
        #check if there is metadata and print if not
        printAllMetadata() if yt.metadata._metadata != [] else print("No metadata found")    


#If the user wants to access the author's channel, it open his browser on it
if(input("Do you want to see more video from " + yt.author + "? (y/n)\n") == "y"):
    webbrowser.open(yt.channel_url)


#If the user wants to access the video's miniature, it open his browser on it
if(input("Do you want to see the miniature of " + yt.title + "? (y/n)\n") == "y"):
    webbrowser.open(yt.thumbnail_url, new=2)

#If the user wants to donwload the video in mp4, it ask him which resolution and download it in the current directory
if(input("Do you want to download " + yt.title + " from " + yt.author + "? (y/n)\n") == "y"):
    my_streams = yt.streams.filter(file_extension='mp4', progressive=True)
    for streams in my_streams:
        print(f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}")

    input_itag = input("Enter itag value for the wanted resolution : ")
    stream = yt.streams.get_by_itag(input_itag)
    stream.download()
    print("\nThe video has been downladed in the current directory\n")