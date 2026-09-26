"""CaesarV2"""
TEXT = input()
wordset = [
    "what", "when", "why", "which",
    "this", "there", "where", "the",
    "is", "am", "are", "you", "we",
    "they", "he", "she", "it"
]

def find_shift(text):
    """find shift value"""
    best_k, max_score = 0, -1
    for k in range(26):
        clean_txt = ''.join(c if c.isalpha() else " " for c in decode(text, k)).lower()
        words_list = clean_txt.split()
        score = 0
        for w in words_list:
            if w in wordset:
                score += 1

        if score > max_score:
            best_k = k
        max_score = max(score, max_score)
    return best_k

def decode(text, k):
    """Shift Text"""
    charset_low, newtext = 'abcdefghijklmnopqrstuvwxyz', ''
    charset_up = charset_low.upper()
    for char in text:
        if char.isalpha():
            useset = charset_low if char.islower() else charset_up
            decoded_index = (useset.index(char) - k) % len(useset)
            newtext += useset[decoded_index]
        else:
            newtext += char
    return newtext

def main():
    """Main function"""
    result = decode(TEXT, find_shift(TEXT))
    print(result)
main()
