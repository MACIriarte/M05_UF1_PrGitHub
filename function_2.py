def DeleteConsonants(phrase):
    consonants = "BCDFGHJKLMNPQRSTVXZWY"
    phrase_without_consonants = ""
    for i in range(0, len(phrase)):
        if str(phrase[i]).upper() in consonants:
            phrase_without_consonants = phrase_without_consonants
        if not str(phrase[i]).upper() in consonants:
            phrase_without_consonants += phrase[i]
    return phrase_without_consonants
