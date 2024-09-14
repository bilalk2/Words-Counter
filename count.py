import re

def count_characters(text):
    """Count all characters including spaces and punctuation."""
    return len(text)

def count_words(text):
    """Count words by splitting on whitespace."""
    words = text.split()
    return len(words)

def count_sentences(text):
    """Count sentences based on punctuation (. ? !) as sentence terminators."""
    sentences = re.split(r'[.!?]+', text)
    return len(sentences) - 1  # Subtract 1 for the last split which is empty

def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    file_path = input("Enter the path of the file: ")
    
    text = read_file(file_path)
    if text is None:
        return
    
    # Count characters, words, and sentences
    num_characters = count_characters(text)
    num_words = count_words(text)
    num_sentences = count_sentences(text)
    
    # Display results
    print("\nFile Analysis:")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")
    print(f"Number of sentences: {num_sentences}")

if __name__ == "__main__":
    main()
