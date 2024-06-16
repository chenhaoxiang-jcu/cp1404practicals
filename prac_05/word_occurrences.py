"""
Word Occurrences
Estimate: 15 minutes
Actual:   9 minutes
"""


def main():
    """Get a string user inputted and count the occurrences of words in a string."""
    text = input("Text: ").split()
    word_to_count = count_word(text)
    word_width = max(len(word) for word in text)
    display_word_and_count(word_to_count, word_width)


def count_word(text):
    """Count the occurrences of words in a string and store them in a dictionary."""
    word_to_count = {}
    for word in sorted(text):
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def display_word_and_count(word_to_count, word_width):
    """Print word and its count neatly."""
    for word, count in word_to_count.items():
        print(f"{word:{word_width}} : {count}")


main()
