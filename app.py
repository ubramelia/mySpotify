
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
spotify_oauth = config['TOKENS']['spotifyAPIToken']
spotify_user = config['DEFAULT']['USER']

