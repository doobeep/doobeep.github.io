# doobeep.github.io
>CS310 Shichao Pei
>Fall 2024, UMASS Boston
need help deciding what to listen to? well... how are you feeling? i'll recommend a song!


## datasets

### **tracks_features.csv**
columns [name,album,artists,energy,valence]

-  name = string representing the song name
-  album = string representing the album of the given song
-  artists = string representing the name of the artist who made the song
-  energy = float/numeric value representing a musical metric for how intense and active a track is. values range from 0.0 to 1.0.
-  valence = float/numeric value representing a musical metric for how positive or negative a track is. values range from 0.0 to 1.0, where 0.0 represents negative emotion and 1.0 represents positive emotion.

### **tracks_features.csv**

columns [name,album,artists,explicit,danceability,key,mode,tempo,year]

-  name = string representing the song name
-  album = string representing the album of the given song
-  artists = string representing the name of the artist who made the song
-  explicit = a binary value (i.e 0 or 1) representing if the track is explict (1) or not (0).
-  danceability = float/numeric value ranging from 0 to 1 representing a spotify metric for how suitable a track is for dancing
-  key = numerical value representing the overall key of the track. values range from 0 to 11. note that key 0 implies musical rest, but is given to tracks with average key values less than 0.50 (meaning for more than half the track, the key was in musical rest. 
-  mode = a binary value (i.e 0 or 1) representing if the track is in major mode (1) or minor mode (0). major and minor modes differ primarily in their emotional connotations. major modes typically evoke feelings of happiness and brightness due to their interval structure, while minor modes convey sadness or introspection.
-  tempo = numerical value representing the overall tempo of a track, in beats per minute (BPM). values range from 0 to 249 BPM.
-  year = four digit numerical value (e.g 'XXXX', 1999) representing the year the song was released.
