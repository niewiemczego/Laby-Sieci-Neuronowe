from collections import Counter
from string import punctuation


def count_words(text: str):
    # ignoruj wielkosc liter text i znaki interpunkcyjne
    text = text.lower()
    text = "".join([c for c in text if c not in punctuation])
    print(text)

    counter = Counter(text.split())

    return (counter.total(), counter, counter.most_common(3))


if __name__ == "__main__":
    text = "przykladowy tekst, w ktorym tekst sie powtarza oraz tekst sie nie powtarza."

    print(count_words(text))
