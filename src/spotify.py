import csv


from collections import namedtuple

spotifyinfo = namedtuple('spotifyinfo','position, artist_name, track_name,track_id,popularity,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature')
                         
def read_3_len(file):
    with open (file, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        info = [spotifyinfo(int(position),artist_name,track_name,track_id,float(popularity),float(danceability),float(energy),float(key),float(loudness),float(mode),float(speechiness),float(acousticness),float(instrumentalness),float(liveness),float(valence),float(tempo),float(duration_ms),int(time_signature)) 
                for position, artist_name,track_name,track_id,popularity,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature in reader]
    totaldisplayed = len(info)
    first3 = info[:3]
    last3 = info[-3:]
    print(totaldisplayed)
    print(first3)
    print(last3)
    





