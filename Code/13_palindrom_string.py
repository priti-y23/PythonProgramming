def is_palindrome_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text