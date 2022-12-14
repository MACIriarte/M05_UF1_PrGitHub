def DeleteVowels(phrase):
    vowels = "AEIOU"
    phrase_without_vowels = ""
    lenght = len(phrase)
    for i in range(0, lenght):
        if str(phrase[i]).upper() in vowels:
            phrase_without_vowels = phrase_without_vowels
        if not str(phrase[i]).upper() in vowels:
            phrase_without_vowels += phrase[i]
    return phrase_without_vowels