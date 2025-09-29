import time
from threading import Thread, Lock
import sys

A = Lock()

def animate_text(text, delay=0.1):
    with A:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print() 

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def Song():
    lyrics = [
        ("\n\nAndai matamu melihat akuuuuu\n", 0.1),
        ("Terungkap semua isi hatikuuuuu\n", 0.1),
        ("Alam sadarku, alam mimpiku\n", 0.1),
        ("Semua milikmu, andai kau tahu\n", 0.1),
        ("Andai kau tahu...\n", 0.1),
        ("Rahasia Cintaku...", 0.25)  
    ]
    
    delays = [1.0, 8.8, 16.5, 19.8, 24.0, 26.5]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    Song()
