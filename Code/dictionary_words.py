import random
import sys

def read_words_file():
    """Read words from the Unix words file."""
    words_list = []
    with open('/usr/share/dict/words', 'r') as file:
        words_list = file.read().splitlines()
    return words_list

def create_random_sentence(num_words, words_list):
    """Create a 'sentence' with the specified number of random words."""
    if num_words > len(words_list):
        return "Error: Requested more words than available"
    
    # Select random words
    selected_words = random.sample(words_list, num_words)
    
    # Join words with spaces and add period at the end
    return ' '.join(selected_words) + '.'

if __name__ == '__main__':
    # Check if number of words argument was provided
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)
    
    try:
        num_words = int(sys.argv[1])
        if num_words < 1:
            print("Please enter a positive number")
            sys.exit(1)
    except ValueError:
        print("Please enter a valid number")
        sys.exit(1)

    # Read words file
    words_list = read_words_file()
    
    # Generate and print random sentence
    sentence = create_random_sentence(num_words, words_list)
    print(sentence)

