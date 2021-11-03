# Programming Fundamentals First Term Project (year 2021/2022)
===============================================================

Author = Raúl Heras Pérez

The aim of this project is to read and analyse the data publshed on the Kaggle data set which can be downloaded [here] (https://www.kaggle.com/rafaelnduarte/spotify-data-with-audio-features?select=world_data.csv). In this data set of 17 columns we can access to the ranking of the most listened songs on Spotify on 2020 in the world, along with several characteristics of the song itself.

## Project folder structure
-----------------------------

- /src: includes the Python modules in which the project is based:
        - spotify.py: Includes functions to access and use the data.
        - spotifytest.py: Includes functions to test `spotify.py` functions.
- /data: includes the dataset of the project:
        - 2020_spotify.csv: File containing the data used in the project.
       
## Dataset structure
------------------------

In this dataset there is contained 17 columns corresponding to the following characteristics of the songs:

- Position: int type, is the position of the song in the ranking.
- Artist(s) name: str type, includes if the song is featured by other artist.
- Track name: srt type, name of the song as shown in Spotify app.
- Track ID: str type, represents the internal name of the track on the Spotify database.
- Popularity: int type, in a scale of 1 to 100, represents the tendency of the Spotify algorithms to include the song in their personal-made playlists such as Weekly Discover.
- Danceability: float type, is a number from 0.0 to 1.0 to describe how suitable the track is to dance to, being 0.0 the least and 1.0 the most danceable track.
- Energy: float type, in a scale from 0.0 to 1.0 describes how fast and noisy the track is in an ascending scale.
- Key: int type, describes in a numeric way in which key the song is written.
- Loudness: float type, is a negative number that measueres the loudness of the audio signal during the mastering process.
- Mode: int type, is a numerical representation of the scale in which the song is written.
- Speechiness: float type, describes the amount of spoken words in a track.
- Acousticness: float type, describes how acoustic a song is, being the most acoustic if the value is 1.0
- Instrumentalness: float type, describes from 0.0 to 1.0 how instrumental a song is.
- Liveness: float type, describes the probability of the song to be recorded with a live audience.
- Valence: float type, from 0.0 to 1.0, describes the overall positive vibe that the song gives. If it is close to 0.0, the track will sound sad or anger and if it is close to 1.0, it will sound happier.
- Tempo: float type,is te tempo of the song expressed in BPM (beats per minute)
- Duration in ms: int type,shows the duration of the songs in miliseconds (ms)
- Time signature: int type,is a notational convention to specify how many beats are in each bar (or measure)

## Implemented types
---------------------

In order to work with the data, a namedtuple has been defined:

<code>spotifyinfo = namedtuple('spotifyinfo','position, artist_name, track_name,track_id,popularity,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature')</code>

in which we can find the following type data:

<code>spotifyinfo(int,str,str,str,int,float,float,int,float,int,float,float,floatfloat,float,float,int,int</code>

## Implemented functions
-------------------------

The following functions have been implemented in this project, clasified in the different modules in which they are implemented and divided by the different deliveries.

#### Module spotify

First delivery
    - read_3_len(file) : reads the data from the csv file and returns the infomation in a list of tuples. It also prints the total number of records read, the first three and the last three elements read.
    
#### Module spotify_test

In this module there has been implemented the test functions for the functions defined in module <code>spotify</code>. For example, <code>read_3_len_test</code> tests the function <code>read_3_len</code>

- read_3_len_test(file)

