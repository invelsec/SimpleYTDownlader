from pytube import YouTube as yt

def downloadVideos(url):
	yt(url).streams.get_highest_resolution().download()
	print(f"Video Title : {yt.title}")
	print(f"Video Author : {yt.author}")
print("Welcome Simple Youtube Downloader")
while True:
	try:
		downloadUrl = input("Give Url : ")
		downloadVideos(str(downloadUrl))
		print("Download Complete.")
	except KeyboardInterrupt:
		print("\nKeyboard Interrupt.. Exiting")
		exit()