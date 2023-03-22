from flask import Flask, request, jsonify
from Sp_text import match_text, yt_transcript, get_show_and_episode
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def hello():
    url = request.json.get("url")
    yturl = url
    yt_text = yt_transcript(yturl)
    show, ep = match_text(yt_text)
    # show, episode = get_show_and_episode(max_link)
    return jsonify({"show": show, "episode": ep})

@app.route("/postData", methods=["POST"])
def post_data():
    return request.json

if __name__ == "__main__":
    app.run(debug=True)