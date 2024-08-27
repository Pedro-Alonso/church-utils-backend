from flask import Blueprint, request, jsonify
from src.services.genius_service import get_lyrics_from_genius

lyrics_bp = Blueprint("lyrics", __name__)

@lyrics_bp.route("/get-lyrics/<string:artist>/<string:title>", methods=["GET"])
def get_lyrics(artist, title):
    client_access_token = request.headers.get("Client-access-token")

    if client_access_token is None:
        return jsonify({"error": "Client-access-token header is missing"}), 400

    lyrics = get_lyrics_from_genius(client_access_token, artist, title)

    if lyrics:
        return jsonify({"lyrics": lyrics}), 200
    else:
        return jsonify({"error": "Song not found"}), 404
