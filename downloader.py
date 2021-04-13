from pytube import YouTube as yt

def downloadVideos(url):
	try:
		yt(url).streams.get_highest_resolution().download()
		print(f"Video Title : {yt.title}\n")
		print(f"Video Author : {yt.author}")
	except Exception:
		print("Error!")
print("Welcome Simple Youtube Downloader")
while True:
	try:
		downloadUrl = input("Give Url : ")
		downloadVideos(str(downloadUrl))
		print("Complete.")
	except KeyboardInterrupt:
		print("\nKeyboard Interrupt.. Exiting")
		exit()