import re

def clean_corpus(file_path):
    """
    Load and clean corpus from file and return it as a list of words.
    
    Args:
        file_path (str): Path to the corpus file
        
    Returns:
        list: Cleaned list of words from the corpus
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return _process_text(file.read())
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        with open(file_path, 'r', encoding='latin-1') as file:
            return _process_text(file.read())
    except Exception as e:
        print(f"Error loading corpus: {e}")
        # Return empty list as fallback
        return []

def _process_text(text):
    """
    Process text with regex cleaning to prepare for Markov chain.
    
    Args:
        text (str): Raw text input
        
    Returns:
        list: Cleaned list of words
    """
    # Replace newlines with spaces
    text = text.replace('\n', ' ')
    
    # Remove chemical formulas, footnotes, and other unusual patterns
    text = re.sub(r'[_\*\[\]\{\}]', ' ', text)  # Remove special characters
    text = re.sub(r'\d+', ' ', text)  # Remove standalone numbers
    text = re.sub(r'([A-Z])(\d)', r'\1 \2', text)  # Separate letters and numbers
    text = re.sub(r'([a-z])(\d)', r'\1 \2', text)  # Separate letters and numbers
    
    # Keep sentence-ending punctuation but remove other punctuation
    text = re.sub(r'[,":;()[\]{}]', ' ', text)
    
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Split into words and remove empty strings or strings with only punctuation
    words = [word for word in text.split() if word and not all(c in '._-–—' for c in word)]
    
    return words