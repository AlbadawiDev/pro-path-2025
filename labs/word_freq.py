from collections import Counter

import re


def word_frequencies(text, limit=10):
    if limit < 0:
        raise ValueError('limit must be non-negative')
    words = re.findall(r"[^\W_]+(?:['’][^\W_]+)?", text.casefold(), flags=re.UNICODE)
    return Counter(words).most_common(limit)


def main():
    for word, count in word_frequencies(input('Pega un párrafo: ')):
        print(f'{word}: {count}')


if __name__ == '__main__':
    main()
