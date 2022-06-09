# -*- coding: utf-8 -*-
"""

@author: Karthik Krishnan 

pafy, youtube_dl, python-vlc , inquirer, rich , youtube-search-python
"""

import pafy 
import vlc 
import urllib.request 
import re 
import inquirer
import sys
from time import sleep
from rich.progress import track, Progress
from youtubesearchpython import PlaylistsSearch
from os import system


played = []
video_ids = []
media = None


def playvideo(url):

    #	ADD URL TO LIST OF PLAYED SONGS
    played.append(url)

    #	INITIALIZE VIDEO
    video = pafy.new(url)
    audio = video.getbestaudio()
    media = vlc.MediaPlayer(audio.url)
    
    media.play()
    
    print("Playing the SONG")
    sleep(100)



    
    '''

    #use this part if you want to see the timestamp of the youtube content

    #	PRINT VIDEO DETAILS
    print(f"\n{'-' * 70}\n")

    print(bcolors.HEADER + "Now Playing: " + bcolors.OKCYAN + video.title)
    print(bcolors.HEADER + "\nViews: " + bcolors.OKCYAN + f"{video.viewcount:,d}")
    print(bcolors.HEADER + "\nDuration: " + bcolors.OKCYAN + video.duration)
    print(bcolors.WARNING + "\nPress 'CTRL+C' to Skip Song!\n" + bcolors.ENDC)

    with Progress(transient=True) as prog:
        song_play = prog.add_task(
            "[green]Playing Song", total=video.length)

        #	START PLAYER
        media.play()

        while media.is_playing() == False:
            pass

        while media.is_playing():
            sleep(1)
            prog.update(song_play, advance=1)

        print(bcolors.OKGREEN + "DONE PLAYING %s!" % video.title)
    '''
    
    
def autoplay(url):
    #	PLAY CURRENT VIDEO
    playvideo(url)

    video_ids = []
    video_ids_dupes = []
    #	CHANGE CURRENT VIDEO TO NEXT ONE
    html = urllib.request.urlopen(url)
    video_ids_dupes = re.findall(
        r"watch\?v=(\S{11})", html.read().decode())

    #	REMOVE DUPLICATES FROM LIST
    for i in video_ids_dupes:
        if "https://www.youtube.com/watch?v=" + i not in played:
            autoplay("https://www.youtube.com/watch?v=" + i)
                
        
def search_youtube(search: str):
    # Check if the given search term is a valid youtube video link
    if(search.startswith("https://www.youtube.com")):
        res = urllib.request.urlopen(search)

        if(res.getcode() == 200):
            return search

    search_url = "https://www.youtube.com/results?search_query={}" + search.replace(" ", "+")

    html = urllib.request.urlopen(search_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = ("https://www.youtube.com/watch?v=" + video_ids[0])
    return url

def play_playlist(url):
    print(url)

    html = urllib.request.urlopen(url)
    video_ids_dupes = re.findall(
        r"watch\?v=(\S{11})", html.read().decode())

    #	REMOVE DUPLICATES FROM LIST
    for i in video_ids_dupes:
        if i not in video_ids and "https://www.youtube.com/watch?v=" + i not in played:
            video_ids.append(i)

    for i in video_ids:
        playvideo("https://www.youtube.com/watch?v=" + i)
        

#	FUNCTION TO TAKE FIRST PLAYLIST FROM YOUTUBE SEARCH PAGE
def search_playlist(search):
    playlistsSearch = PlaylistsSearch(search, limit=1)
    play_playlist(playlistsSearch.result()["result"][0]["link"])


if __name__== "__main__":

    #search="banja rani"
    #url = search_youtube(search) 
    
    search = "latest hindi"
    url = search_playlist(search)
    print(url)


    #playvideo(url)
    try:
        #playvideo(url)#play song alone
        #autoplay(url)#play song autoplay
        play_playlist(url)
        
    except KeyboardInterrupt:
        media.stop()
        del media
        exit()
    
    
    
    
