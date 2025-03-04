"""Main script, uses other modules to generate sentences."""
from flask import Flask
from markov_chain import MarkovChain
from text_cleaner import clean_corpus

app = Flask(__name__)


# Try to load the corpus, or use a backup text if it fails
try:
    corpus_path = 'data/dracula.txt'
    word_list = clean_corpus(corpus_path)
    print(f"Loaded {len(word_list)} words from {corpus_path}")
except Exception as e:
    print(f"Error loading corpus: {e}")
    # Use a backup text if the corpus loading fails
    fish_text = 'one fish two fish red fish blue fish'
    word_list = fish_text.split()


# initialize the Markov chain
markov_chain = MarkovChain(word_list)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # Generate a sentence with 15 words
    sentence = markov_chain.generate_sentence(num_words=15)
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Markov Chain Text Generator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
            }}
            h1 {{
                color: #333;
            }}
            .generated-text {{
                font-size: 18px;
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <h1>Markov Chain Text Generator</h1>
        <div class="generated-text">
            <p>{sentence}</p>
        </div>
        <p>This text was generated using a Markov Chain model trained on Bram Stoker's Dracula.</p>
        <p>Refresh the page to generate a new sentence!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
    To learn more about Flask's DEBUG mode, visit
    https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)