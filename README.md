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
- Mode: int type, is a 
- ,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature

