
import requests
import json

class SpotifyConsole:
    """This is the spotify client interface rest API thing"""

    def __init__(self, oauthtoken, userID):
        """
        param (str) oauthtoken = the spotify API authentication token
        param (str) userID = your spotify userID
        """
        self._oauthtoken = oauthtoken
        self._userID = userID
        
    def _spotify_get_request(self, url):
        """this sends a get request to spotify client at url"""
        response = requests.get(
            url,
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._oauthtoken}"
            }
        )
        data = response.json()
        return data

    def _get_user_playlist(self, userID, limit):
        """this gets user's playlist w/ a limit"""
        response = requests.get(
            url = f"https://api.spotify.com/v1/users/{userID}/playlists?limit={limit}",
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._oauthtoken}"
            }
        )
        data = response.json()
        return data

    def _get_user_recent_track(self, limit):
        """This will get the user's playlist w/ a limit"""
        response = requests.get(
            url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}",
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._oauthtoken}"
            }
        )
        data = response.json()
        return data

    def _create_user_playlist(self, userID, playlistName, playlistDesc):
        """this creates a new user playlist for the user"""
        data = json.dumps({
            "name": playlistName,
            "description": playlistDesc
        })
        response = requests.post(
            url = f"https://api.spotify.com/v1/users/{userID}/playlists",
            data = data,
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._oauthtoken}"
            }
        )
        data = response.json()
        return data
