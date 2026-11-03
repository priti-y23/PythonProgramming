def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants