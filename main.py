from flask import Flask, jsonify
from flask_cors import CORS
from masterlist import MASTER_LIST

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
  dict = {}
  for song in MASTER_LIST:
    dict[song.dict["name"]] = song.dict
  return dict


import urllib.request
for song in MASTER_LIST:
  for entry in ["primo", "secondo", "both"]:
    urllib.request.urlretrieve(song.dict[entry]['pdf'], song.dict["name"] + " " + entry + " pdf.pdf")
    urllib.request.urlretrieve(song.dict[entry]['audio'], song.dict["name"] + " " + entry + " audio.mp3")


if __name__ == '__main__':
    app.run(host='0.0.0.0')