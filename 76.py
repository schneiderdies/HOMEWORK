from string import punctuation

def tokenize(text):
    for punct_c in punctuation:
        string = text.replace(punct_c, ' ')
    string_tokens = string.split()
    return string_tokens

string = "the cat sat on the mat"
print(tokenize(string))
