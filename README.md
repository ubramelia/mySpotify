# mySpotify

Using Spotify Rest API for the first time.

1. Create spotify account
2. go to developer spotify site
3. get auth token for whatever you want to do
3. create config.ini file containing your username, userID, etc.  It will look like this...
```
[DEFAULT]
USER = putUserNameHere
USERID = putUserIDHere
PLAYLISTNEWNAME = NameOfNewPlaylistHere
PLAYLISTDESC = Write a description for the new playlist here.

[TOKENS]
spotifyAPIToken = XXX <- secret Authentication token thing from spotify website

[QUERYSETTINGS]
PLAYLISTLIMIT = # <- # of playlists you want it to output.
TRACKLIMIT = # <- # of tracks you want it to output.
```
4. save all that.
5. run app.py