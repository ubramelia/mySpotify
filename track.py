
class Track:
    """reprsents a track :("""

    def __init__(self, trackID, trackName, artistName, albumName):
        """
            param (str) trackID = you know wtf this is
            param (str) trackName = the name, idiot
            param (str) artistName = the artist (not id, bro)
            param (str) albumName = wtf do you think (not id, bro)
        """
        self._trackID = trackID
        self._trackName = trackName
        self._artistName = artistName
        self._albumName = albumName

    def __str__(self):
        string = f"The Track ID is {self._trackID} \nThe Track Name is {self._trackName} \nThe Artist name is {self._artistName} \nThe album name is {self._albumName}"
        return string