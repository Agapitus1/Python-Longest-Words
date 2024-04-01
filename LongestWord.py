import sys

for line in sys.stdin:
    words = line.split()
    longest_word = max(words, key=len)
    print(longest_word)
