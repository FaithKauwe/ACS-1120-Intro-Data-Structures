"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

fish_text = 'one fish two fish red fish blue fish'
histogram = Dictogram(fish_text.split())

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    random_word = histogram.sample()
    return f"<p>Random word: {random_word}</p>"



if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
