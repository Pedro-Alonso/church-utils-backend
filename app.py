from flask import Flask
from flask_cors import CORS
from src.routes import lyrics
from src.routes import helloworld

app = Flask(__name__)
CORS(app)

app.register_blueprint(helloworld.helloworld_bp)
app.register_blueprint(lyrics.lyrics_bp)

if __name__ == "__main__":
    app.run(debug=True)
