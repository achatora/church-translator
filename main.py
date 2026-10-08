from features.translation.text import clean_text
from features.translation.translator import translate


def main() -> None:

    english_text = input("Enter English text: ")
    cleaned_text = clean_text(english_text)

    if not cleaned_text:
        print("No text to translate.")
        return

    polish_text = translate(cleaned_text)

    print(polish_text)


# Run the program when this file is executed directly
if __name__ == "__main__":
    main()
