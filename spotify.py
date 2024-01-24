import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


SONGS = 10

artis = input("artista:   ")
reproduccion = []

add_song = True

def tracks_time(tracks, my_list):
    print("\n\ntu lista")
    play_duration = 0
    for i in my_list:
        track = next((d for d in tracks if d.get("id") == i), None)
        time = int(track['duration_ms'])/60000
        print("{} : {:.2f}".format(track['name'],round(time,2)))
        play_duration +=time
    print("Duracion play list : {:.2f} min".format(round(play_duration,2)))

def top_song(results):
    top_song_artist = []
    for idx, track in enumerate(results['tracks']['items']):
        song_dict = {'id':idx+1, 'name':track['name'], 'popularity':track['popularity'], 'duration_ms':track['duration_ms']}
        top_song_artist.append(song_dict)
    
    return top_song_artist

def print_songs(tracks):
    print("top canciones:")
    for track in tracks:
        print(f"{track['id']} {track['name']} \t popularity {track['popularity']}")

try:
    f = open("credentials.txt", "r")
    client_id =f.readline()
    client_secret=f.readline()
    f.close()
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
    results = sp.search(q=artis, limit=SONGS)
    tracks = top_song(results)
    print_songs(tracks)
    print("\n\nArma tu lista de reproduccion :)")
    while add_song:
        number = int(input("numero cancion: "))
        reproduccion.append(number)
        other_song = input("agregar otra cancion y/n:  ")
        if other_song == 'n':
            add_song = False
    tracks_time(tracks, reproduccion)
except Exception as err:
    print(err)
