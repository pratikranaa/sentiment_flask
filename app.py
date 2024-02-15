from flask import Flask, request, render_template
from models import sentiment

app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        text = request.form["message"]
        result = sentiment.get_sentiment(text)
        return render_template("result.html", result=result)
    
if __name__ == "__main__":
    app.run(debug=True)