original = ""
# test_text = "Lorem ipsum dolor sit amet nostrud ea in ad sunt consectetur ad magna sunt eiusmod est minim ad cillum exercitation eiusmod laboris tempor. Aliqua veniam exercitation eiusmod consequat deserunt et amet labore nulla dolor."
# test_text = "Lorem ipsum dolor sit amet nostrud ea in ad sunt consectetur ad magna sunt, eiusmod est minim ad cillum exercitation eiusmod laboris tempor. Aliqua veniam exercitation eiusmod consequat! Deserunt et amet labore nulla dolor?"
# test_text = "Lorem ipsum dolor sit amet nostrud ea in ad sunt consectetur ad magna sunt eiusmod est minim ad cillum exercitation eiusmod laboris tempor."
test_text = "The quick brown fox jumps over the lazy dog."
vowels = "aeiou"
spec_char = ",.?!:;"

try:
    while True:
        original = input("\nEnter a sentence (for default, press Enter): ").strip() or test_text
        print(f"\n{original}")
        words = original.split()
        new_words = []

        for word in words:
            punctuation = ""
            first_word = False

            if word.istitle():
                first_word = True

            for char in word:
                if char in spec_char:
                    char_place = word.index(char)
                    punctuation = word[char_place]
                    word = word.strip(char)

            if word[0] in vowels:
                if first_word:
                    word = word.title()
                new_words.append(word + "yay")
            else:
                vowel_position = 0
                for letter in word:
                    if letter not in vowels:
                        vowel_position += 1
                    else:
                        break
                first_syllable = word[:vowel_position]
                rest_of_word = word[vowel_position:]
                new_word = rest_of_word + first_syllable + "ay"
                if first_word:
                    new_word = new_word.title()
                new_words.append(new_word + punctuation)                
        new_sentence = ""

        for new_word in new_words:
            new_sentence += new_word + " "

        print(f"\n{new_sentence.strip()}")

except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
