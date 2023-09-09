from time import sleep

song = input("Copy Paste the lyrics of the song -->")
listsong = song.split()
for i in range(len(listsong)):
    print(listsong[i])
    sleep(0.4)

    


