def uppercase(text):          # Converts string to uppercase
    return text.upper()

def lowercase(text):          # Converts string to lowercase
    return text.lower()

def concatenate(text1, text2):   # Joins two strings
    return text1 + text2

def replace_word(text, old, new):   # Replaces part of string
    return text.replace(old, new)

def reverse_string(text):     # Reverses the string
    return text[::-1]

def string_length(text):      # Returns length of string
    return len(text)

if __name__ == '__main__':

    text = "Hello World"

    upper = uppercase(text)
    print(upper)

    lower = lowercase(text)
    print(lower)

    joined = concatenate("Python ", "Programming")
    print(joined)

    replaced = replace_word(text, "World", "Python")
    print(replaced)

    reversed_text = reverse_string(text)
    print(reversed_text)

    length = string_length(text)
    print(length)