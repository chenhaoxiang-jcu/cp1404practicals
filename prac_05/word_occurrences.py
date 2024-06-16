"""
Word Occurrences
Estimate: 15 minutes
Actual:   9 minutes
"""

word_to_count = {}
text = input("Text: ").split()
word_width = max(len(word) for word in text)

for word in sorted(text):
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in word_to_count.items():
    print(f"{word:{word_width}} : {count}")
