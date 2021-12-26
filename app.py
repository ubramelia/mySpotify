
import json
import configparser
from spotifyconsole import SpotifyConsole
from track import Track

config = configparser.ConfigParser()
config.read('config.ini')
spotify_oauth = config['TOKENS']['spotifyAPIToken']
spotify_user = config['DEFAULT']['USER']
spotify_userID = config['DEFAULT']['USERID']
spotify_playlist_limit = config['QUERYSETTINGS']['PLAYLISTLIMIT']
spotify_track_limit = config['QUERYSETTINGS']['TRACKLIMIT']
spotify_playlist_new_name = config['DEFAULT']['PLAYLISTNEWNAME']
spotify_playlist_new_desc = config['DEFAULT']['PLAYLISTDESC']

spotifyConsoleObj = SpotifyConsole(spotify_oauth, spotify_user)
url = f"https://api.spotify.com/v1/me/playlists?limit={spotify_playlist_limit}"

trackObj = Track("a", "b", "c", "d")

data = spotifyConsoleObj._spotify_get_request(url)
more_data = spotifyConsoleObj._get_user_playlist(spotify_userID, spotify_playlist_limit)
track_data = spotifyConsoleObj._get_user_recent_track(spotify_track_limit)
even_more_data = spotifyConsoleObj._create_user_playlist(spotify_userID, spotify_playlist_new_name, spotify_playlist_new_desc)

with open('playlist.json', 'w') as outfile:
    json.dump(data, outfile)

with open('userIDplaylist.json', 'w') as outfile:
    json.dump(more_data, outfile)

with open('recenttrack.json', 'w') as outfile:
    json.dump(track_data, outfile)

with open('newplaylist.json', 'w') as outfile:
    json.dump(even_more_data, outfile)

print(trackObj)