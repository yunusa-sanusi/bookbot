def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        num_of_text, text_count = get_text(file_contents)
        print(num_of_text)
        for text in text_count:
            print(f'The character {text} was found {text_count[text]} times')


def get_text(book: str):
    text_count_dict = {}
    text_list = book.split()
    converted_text = book.lower()
    for text in converted_text:
        text_count_dict[text] = converted_text.count(text)

    return len(text_list), text_count_dict


main()
