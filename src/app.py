import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

import os
import matplotlib.pyplot as plt
# Inicializar la biblioteca Spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
# top 10 de sus canciones
satyricon_uri = 'spotify:artist:221Rd0FvVxMx7eCbWqjiKd'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = client_id,client_secret =client_secret))

best_10=spotify.artist_top_tracks(satyricon_uri)
# Transformar a Pandas DataFrame
song=[]
popular=[]
duration=[]
for track in best_10['tracks'][:10]:
    for i,val in enumerate(best_10['tracks'][0]):
        if i==3:
            duration.append(track['duration_ms'])
        if i==11:
            song.append(track['name'])
        if i==12:
            popular.append(track['popularity'])    
data={'Titulo_Cancion':song,'Popularidad':popular,'Duracion (Min)':duration}
df_best_10=pd.DataFrame(data)
df_best_10['Duracion (Min)']=df_best_10['Duracion (Min)'].multiply(0.00001666667) 
df_best_10 = df_best_10.sort_values(by=['Popularidad']) 
df_best_10.reset_index(inplace=True)
df_best_10 = df_best_10.drop(['index'],axis=1)
df_best_10.tail(3)
df_best_10
# Visualizacion

sns.scatterplot(x=df_best_10['Popularidad'], y=df_best_10['Duracion (Min)'])
plt.show()

# Analizar relación estadística
print('Se evidencia que la duracion de la cancion no tiene relacion directa con la popularidad de las canciones.')