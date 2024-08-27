import lyricsgenius
from src.utils import sanitize_param


def get_lyrics_from_genius(client_access_token, artist, title):
    genius = lyricsgenius.Genius(client_access_token)
    sanitized_artist = sanitize_param.run(artist)
    sanitized_title = sanitize_param.run(title)
    song = genius.search_song(artist=sanitized_artist, title=sanitized_title)
    return song.lyrics if song else None
