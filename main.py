def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    words = get_words(text)
    chars = get_each_char_count(text)
    sorted_chars = sort_dict(chars)
    print(f"Begin report of {path}")
    print(f"Words: {words}")
    print("Character count:")

    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char} : {count}")

    print("End of report")

def get_text(path):
    with open(path) as f:
        return f.read()


def get_words(text):
    return len(text.split())


def get_each_char_count(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_dict(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)

main()
