#The code goes to the music directory containing all the songs you want to play,
#and puts them all in a list. 
#Then it randomly plays each song one after the other.
import random, os
music_dir = 'E:\\music diretory'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

# Prints The Song Name
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[0])) 