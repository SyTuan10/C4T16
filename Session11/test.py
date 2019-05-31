from __future__ import unicode_literals
import youtube_dl
import json

song_title = []
song_id = []
song_title = []
song_creator = []
song_duration = []
song_library = {
    "song_title": song_title,
    "song_id": song_id,
    "song_title": song_title,
    "song_creator": song_creator,
    "song_duration": song_duration
}

while True:
    print("""Hello! This is TK music app
            Pick one of the options: 
            1. Show All songs
            2. Detail of a song
            3. Play a song
            4. Search and download songs
            5. Exit
            
            
            """ )
    choice_1 = int(input(">>> "))

    if choice_1 == 4:
    # Search and download song and add to song_library
        ydl_opts = {
            "default_search": "ytsearch1",
        }
        search = input("Enter a song to search: ")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # Data as dictionary is stored in variable result
            result = ydl.extract_info(
                "https://www.youtube.com/results?search_query=" + search,
                download=False
            )
            # Convert dictionary into json. Data stored in result is in json 
        # data is key
        
        # print(result['entries'][0]["id"])
        with open('data.json', 'w') as outfile:
            json.dump(result, outfile)
        
        for i in range(len(result["entries"])):
            # i is the index of the song in entries
            print(str(i + 1) + "." + result["entries"][i]["title"])
        song_download_number = int(input("""Enter a song position you want to download.
    >>> """))
        

            
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result_download_song = ydl.download(["https://www.youtube.com/watch?v=" + result["entries"][song_download_number - 1]["id"]])
            # with open('song.json', 'w') as outfile:
            #    json.dump(result_download_song, outfile)
            
            print(result["entries"][song_download_number - 1]["title"]+ " has been downloaded")
        
        
        song_title.append(result["entries"][song_download_number - 1]["title"])
        song_id.append(result["entries"][song_download_number -1]["id"])
        song_creator.append(result["entries"][song_download_number -1]["creator"])
        song_duration.append(result["entries"][song_download_number -1]["duration"])
    if choice_1 == 1:
        if len(song_title) == 0:
            choice_11 = input("""Song list is empty.
    Press Enter to continue...""")
        if choice_11 == "":
            continue
        elif len(song_title) > 0:
            for i, item in enumerate(song_title):
                print(str(i + 1) + "." + item)
            
    if choice_1 == 2:
        if len(song_title) == 0:
            choice_12 = input("""No song to show.
            Press enter to continue...""")
        if choice_12 == "":
            continue
        elif len(song_title) > 0:
            # Need to match song_detail_number(seen in song list) to index of the song
            song_detail_number = int(input("Enter song number to show detail: "))
            
            print("ID: " + song_id[song_detail_number - 1])
            
            print("TITLE: " + song_title[song_detail_number - 1])
            
            print("CREATOR: " + str(song_creator[song_detail_number - 1]))
            
            print("DURATION: " + str(song_duration[song_detail_number -1]))
    if choice_1 == 3:
        if len(song_title) == 0:
            choice_13 = input("""No song to play.
            Press enter to continue...
            """)
        if choice_1 == "":
            continue
        elif len(song_title) > 0:
            song_play_number = int(input("Enter song number you want to play: "))
            # print(result["entries"][song_play_number -1]["title"] + "-" + result["entries"][song_play_number -1]["id"] + ".mp4")
            import pyglet
            # music = pyglet.resource.media(result["entries"][song_play_number -1]["title"] + "-" + result["entries"][song_play_number -1]["id"] + ".mp4")
            music = pyglet.resource.media(song_title[song_play_number - 1] + "-" + song_id[song_play_number - 1] + ".mp4")
            music.play()
            pyglet.app.run()
            continue
    if choice_1 == 5:
        break