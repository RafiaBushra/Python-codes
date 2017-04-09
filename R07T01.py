def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            key = input("Give the word to be added in English: ")
            value = input("Give the word to be added in Spanish: ")
            english_spanish[key] = value

        elif command == "R":
            key = input("Give the word to be removed: ")
            if key in english_spanish:
                del english_spanish[key]
            else:
                print("The word", key, "could not be found from the dictionary.")

        elif command == "P":
            for key, value in sorted(english_spanish.items()):
                print(key, " ", value)

        elif command == "T":
            sentence = (input("Enter the text to be translated in Spanish: ")).split()
            print("The text, translated by the dictionary:")
            for index in range(len(sentence)):
                if sentence[index] in english_spanish:
                    sentence[index] = english_spanish[sentence[index]]
            translated_sentence = ""
            for index in range(len(sentence)):
                translated_sentence += sentence[index] + " "
            translated_sentence = translated_sentence.rstrip()
            print(translated_sentence)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
