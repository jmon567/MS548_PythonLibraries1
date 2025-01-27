# Import the necessary libraries
from textblob import TextBlob
from googletrans import Translator
from PyDictionary import PyDictionary

#display the menu options for the text processing tasks
def display_menu():
    """
    Display the menu options for the text processing tasks.
    """
    print("\nText Processing Menu:")
    print("1. Sentiment Analysis")
    print("2. Language Translation")
    print("3. Spelling Correction")
    print("4. Noun Phrase Extraction")
    print("5. Word Definitions")
    print("6. Exit")

#main function to run the menu-driven program
def main():
    """
    Main function to run the menu-driven program.
    """
    while True:
        # Display the menu
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        # Perform the selected task
        if choice == '1':
            sentiment_analysis()
        elif choice == '2':
            language_translation()
        elif choice == '3':
            spelling_correction()
        elif choice == '4':
            noun_phrase_extraction()
        elif choice == '5':
            word_definitions()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#function to prompt the user to go back to the main menu
def go_back_to_menu():
    """
    Prompt the user to go back to the main menu.
    """
    input("\nPress Enter to go back to the main menu...")

#function to perform sentiment analysis on a user-provided text
def sentiment_analysis():
    """
    Perform sentiment analysis on a user-provided text.
    """
    text = input("Enter a text for sentiment analysis: ")
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"Sentiment: {sentiment}")
    go_back_to_menu()

#function to translate a user-provided text to a specified language
def language_translation():
    """
    Translate a user-provided text to a specified language.
    """
    text = input("Enter a text to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish): ")
    blob = TextBlob(text)
    translator = Translator()
    translated_blob = translator.translate(str(blob), dest=target_language)
    #translated_blob = blob.translate(to=target_language)
    print(f"Translated text: {translated_blob}")
    go_back_to_menu()

#function to perform spelling correction on a user-provided text
def spelling_correction():
    """
    Perform spelling correction on a user-provided text.
    """
    text = input("Enter a text for spelling correction: ")
    blob = TextBlob(text)
    corrected_text = blob.correct()
    print(f"Corrected text: {corrected_text}")
    go_back_to_menu()

#function to extract noun phrases from a user-provided text
def noun_phrase_extraction():
    """
    Extract noun phrases from a user-provided text.
    """
    text = input("Enter a text to extract noun phrases: ")
    blob = TextBlob(text)
    noun_phrases = blob.noun_phrases
    print("Noun Phrases:")
    for phrase in noun_phrases:
        print(f"- {phrase}")
    go_back_to_menu()

#function to provide definitions for words in a user-provided text
def word_definitions():
    """
    Provide definitions for words in a user-provided text.
    """
    text = input("Enter a text to get word definitions: ")
    dictionary = PyDictionary()
    words = text.split()
    print("Word Definitions:")
    for word in words:
        definition = dictionary.meaning(word)
        if definition:
            print(f"{word}: {definition}")
        else:
            print(f"{word}: No definition found")
    
    print("This function is not available at this time.")
    go_back_to_menu()

# Run the main function to start the program
if __name__ == "__main__":
    main()
