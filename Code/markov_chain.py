from dictogram import Dictogram
import random

class MarkovChain:
    def __init__(self, word_list):
        """Initialize a Markov Chain with a list of words."""
        self.markov_dict = {}
        self.build_markov_dict(word_list)

    def build_markov_dict(self, word_list):
        """Build a dictionary that maps each word to a Dictogram of its possible next words."""
        # each word is the key and a dictogram is it's value. the dicto is another nested dict with keys being words that come after 
        # og word and values being numerical probability of occurrence
        for i in range(len(word_list) - 1):
            current_word = word_list[i]
            next_word = word_list[i + 1]
            
            # if we've seen this word before, add the next word to its dictogram
            # in the nested key value pair
            if current_word in self.markov_dict:
                self.markov_dict[current_word].add_count(next_word)
            # otherwise, create a new dictogram with the next word
            else:
                self.markov_dict[current_word] = Dictogram([next_word])
    
    def generate_sentence(self, num_words=10):
        """Generate a sentence with the specified number of words."""
        if not self.markov_dict:
            return "No words in the corpus"
            
        sentence = []
        # the keys in self.markov_dict are all the unique words in the corpus
        current_word = random.choice(list(self.markov_dict.keys()))
        # create list of words that start with uppercase
        capitalized_words = [word for word in self.markov_dict.keys() if word and isinstance(word, str) and word[0].isupper()]
        # if list is populated replace starting word with word from capitalixed_words list
        if capitalized_words:
            current_word = random.choice(capitalized_words)
        
        sentence.append(current_word)
        
        # generate the rest of the sentence
        for _ in range(num_words - 1):
            if current_word in self.markov_dict:
                # use the Dictogram's sample method to select the next word based on frequency, using the numerical probability values
                next_word = self.markov_dict[current_word].sample()
                sentence.append(next_word)
                current_word = next_word
            else:
                # if we reach a word with no followers, choose another random word
                current_word = random.choice(list(self.markov_dict.keys()))
                sentence.append(current_word)
        
        
        # check if last word in sentence actually a string with isinstance
        # then check if last char in last word of sentence already has punctuation
        if isinstance(sentence[-1], str) and sentence[-1][-1] not in [".", "!", "?"]:
        # if both conditions are true (str and no punctuation), add random choice of closing punctuation
            sentence[-1] = sentence[-1] + random.choice([".", "!", "?"])
        
        return " ".join(sentence)