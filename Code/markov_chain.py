from dictogram import Dictogram
import random

class MarkovChain:
    def __init__(self, word_list):
        """Initialize a Markov Chain with a list of words."""
        self.markov_dict = {}
        self.build_markov_dict(word_list)

    def build_markov_dict(self, word_list):
        """Build a dictionary that maps each word to a Dictogram of its possible next words."""
        for i in range(len(word_list) - 1):
            current_word = word_list[i]
            next_word = word_list[i + 1]
            
            # If we've seen this word before, add the next word to its dictogram
            if current_word in self.markov_dict:
                self.markov_dict[current_word].add_count(next_word)
            # Otherwise, create a new dictogram with the next word
            else:
                self.markov_dict[current_word] = Dictogram([next_word])
    
    def generate_sentence(self, num_words=10):
        """Generate a sentence with the specified number of words."""
        # Start with a random word
        if not self.markov_dict:
            return "No words in the corpus"
            
        sentence = []
        current_word = random.choice(list(self.markov_dict.keys()))
        
        # Try to start with a capitalized word if possible
        capitalized_words = [word for word in self.markov_dict.keys() if word and isinstance(word, str) and word[0].isupper()]
        if capitalized_words:
            current_word = random.choice(capitalized_words)
        
        sentence.append(current_word)
        
        # Generate the rest of the sentence
        for _ in range(num_words - 1):
            if current_word in self.markov_dict:
                # Use the Dictogram's sample method to select the next word based on frequency
                next_word = self.markov_dict[current_word].sample()
                sentence.append(next_word)
                current_word = next_word
            else:
                # If we reach a word with no followers, choose another random word
                current_word = random.choice(list(self.markov_dict.keys()))
                sentence.append(current_word)
        
        # Add proper punctuation to the end of the sentence if needed
        if isinstance(sentence[-1], str) and sentence[-1][-1] not in [".", "!", "?"]:
            sentence[-1] = sentence[-1] + random.choice([".", "!", "?"])
        
        return " ".join(sentence)