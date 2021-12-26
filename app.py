
import json
import configparser
from spotifyconsole import SpotifyConsole

config = configparser.ConfigParser()
config.read('config.ini')
spotify_oauth = config['TOKENS']['spotifyAPIToken']
spotify_user = config['DEFAULT']['USER']
spotify_userID = config['DEFAULT']['USERID']
spotify_playlist_limit = config['QUERYSETTINGS']['PLAYLISTLIMIT']

spotifyConsoleObj = SpotifyConsole(spotify_oauth, spotify_user)
url = f"https://api.spotify.com/v1/me/playlists?limit={spotify_playlist_limit}"

data = spotifyConsoleObj._spotify_get_request(url)
more_data = spotifyConsoleObj._get_user_playlist(spotify_userID, spotify_playlist_limit)

with open('playlist.json', 'w') as outfile:
    json.dump(data, outfile)

with open('userIDplaylist.json', 'w') as outfile:
    json.dump(more_data, outfile)
