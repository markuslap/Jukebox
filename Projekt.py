import os, vlc, time
from mutagen.mp3 import MP3

#tuleb importida pip-ga python-vlc package ja mutagen package!!


def read_the_songs():
    def list():
        music=link
        rough_list=os.listdir(music)
        a=1
        names=''
        for i in rough_list:
            name=str(a)+' - ' +i+('\n')
            names+=name
            a+=1
        return [names,rough_list]

    def dictonary(rough_list):
        a=1
        right_folders={}
        for i in rough_list:
            right_folders[str(a)]=os.path.abspath(link)+'\\'+i
            a+=1
        
        return(right_folders)
    styles=dictonary(list()[1])
    
    folder=input('Millist muusikat soovite kuulata?\n'+ list()[0] +'\nSisestage vastav number: ')

    f=styles[folder]
  
    return f

def järjestamine(song_list, songs):
    a=[]
    right={}
    
    for i in range(len(songs)):
        sum=0
        for j in (song_list):
            sum+=j[i]
        a+=[sum]
        
    for n in range(len(songs)):
        right[songs[n]]=a[n]
    final_dict=sorted(right, key=right.get)
    final_dict.reverse()
    
    return(final_dict)

def voting(n):
    songs=os.listdir(n)
    voters=int(input('Sisesta hääletajate arv: '))
    
    song_votes=[]
    while voters>0:
        votes=[]
        for song in songs:
            song=song.replace('.mp3',' ').replace('.wav',' ')
            while True:
                try:
                    vote=int(input('Hinda laulu '+ song+ 'skaalal 1-5: '))
                    if vote<=5 and vote>=1:
                        votes+=[vote]
                        break
                    else:
                        print('Andsid sobimatu hinde... \nProovi uuesti!')
                except:
                    print('Andsid sobimatu hinde... \nProovi uuesti!')
        song_votes+=[votes]
        voters-=1
        if voters!=0:
            print('\nJärgmise hääletaja kord!\n')
        else:
            print('\nHääletatud!')

    return järjestamine(song_votes, songs)

link=os.path.abspath('Projekt.py').replace('Projekt.py','music')
n=read_the_songs()

songs_list=[]

for i in voting(n):
    next_song=os.path.abspath(n) +'\\'+i
    songs_list+=[next_song]
    

for j in songs_list:
    audio=MP3(j)
    duration=audio.info.length
    p=vlc.MediaPlayer(j)
    p.play()
    time.sleep(duration)

        
        