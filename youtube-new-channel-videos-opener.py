import requests
import webbrowser
import time

apiKey = "[YOUR API KEY]"

while True:
    # podanie przez użytkownika nazwy kanału i ilości najnowszych filmików do otwarcia
    channel_name = input("Please enter the name of the Youtube channel: ")
    try:
        videos_count = int(input("How many newest videos would you like to open in new tabs: "))
    except:
        print("Wrong input. Assumed videos count = 1")
        time.sleep(1)
        videos_count = 1
    # parametry URL JSON
    parametersToGetId_dict = {
                    "part": "contentDetails",
                    "forUsername": channel_name,
                    "key": apiKey
                    }
    # pobranie ID kanału na podstawie jego nazwy
    try:
        channel_data = requests.get("https://www.googleapis.com/youtube/v3/channels", parametersToGetId_dict).json()
        channel_id = channel_data["items"][0]["id"]
        break
    except:
        print("Wrong channel name, please try again")
        print()
        continue
    
# parametry URL JSON
parametersNewestVideos_dict = {
                            "key": apiKey,
                            "channelId": channel_id,
                            "order": "date",
                            "part": "snippet",
                            "type": "video",
                            "maxResults": videos_count
                        }
# pobranie ID najnowszych filmów na podstawie ID kanału
channel_videos = requests.get("https://www.googleapis.com/youtube/v3/search", parametersNewestVideos_dict).json()
# stworzenie listy z ID najnowszych filmów
videoIdList = []
for videos_dict in channel_videos["items"]:
    videoIdList.append(videos_dict["id"]["videoId"])
# otwarcie linków w nowych zakładkach
for videoIds in videoIdList:
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=" + videoIds)