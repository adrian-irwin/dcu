# Define a function called get_plural().
# The function should have one parameter which is a word (a noun) and the function should return the plural of the word based on the following rules:
# Add es if the noun ends in ch, sh, x, s or z.
# If a noun ends in a consonant + y drop the y and add ies.
# If a noun ends in f (or fe) drop the f (or fe) and add ves.
# If a noun ends in o add es.
# Otherwise add s.

def get_plural(word):
    if word.endswith(("ch", "sh", "x", "s", "z")):
        return word + "es"
    elif word.endswith("y") and not (word[-2] in "aeiou"):
        return word[:-1] + "ies"
    elif word.endswith("f"):
        return word[:-1] + "ves"
    elif word.endswith("fe"):
        return word[:-2] + "ves"
    elif word.endswith("o"):
        return word + "es"
    else:
        return word + "s"
