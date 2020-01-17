def make_album(artist_name, album_name, number_of_tracks=''):
    album = {'Artist' : artist_name , 'Album' : album_name,}
    if number_of_tracks:
        album['Tracks'] = number_of_tracks
    return album

print(make_album('Led Zeppelin', 'In through the out door'))
print(make_album('The Beatles', 'The White Album', number_of_tracks=30))
print(make_album('Slayer', 'Reign in Blood'))



