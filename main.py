from features.translation.text import clean_text


def main() -> None:

    english_text = input("Enter English text: ")
    english_text = clean_text(english_text)

    if not english_text:
        print("No text to translate.")
    else:
        print(english_text)


# Start the program only if this is
# the file I chose to run or execute
if __name__ == "__main__":
    main()
