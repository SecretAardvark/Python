def make_album(artist_name, album_name, number_of_tracks=''):
    album = {'Artist' : artist_name , 'Album' : album_name,}
    if number_of_tracks:
        album['Tracks'] = number_of_tracks
    return album





 
  
while True:

    print("\nTell me a favorite music album!")
    print("Type 'q' at any time to quit.")
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break

    print(make_album(artist, album))

    
    

     